import curses
import time

from components import get_component

from build.simulink import *


class Editor:
    x = 0
    y = 0

    class StatusBar:
        def __init__(self, start_y, start_x, height, width):
            self.window = curses.newwin(height, width, start_y, start_x)
            self.window.box()
            self.window.refresh()

        def show_message(self, message):
            self.window.clear()
            self.window.box()
            self.window.addstr(1, 1, message)
            self.window.refresh()

    def __init__(self, stdscr, grid):
        self.stdscr = stdscr
        self.main_window_height = curses.LINES - 3
        self.main_window_width = curses.COLS
        self.status_bar = Editor.StatusBar(self.main_window_height, 0, 3, self.main_window_width)
        stdscr.resize(self.main_window_height, self.main_window_width)
        self.grid = grid

    def edit_mode(self):
        self.status_bar.show_message("Edit mode")
        while 1:
            for _y in range(self.main_window_height - 1):
                for _x in range(self.main_window_width - 1):
                    s = self.grid.get(_x, _y)
                    self.stdscr.addstr(_y, _x, str(s))

            self.stdscr.move(self.y, self.x)

            key = self.stdscr.getch()

            # Cursor movement
            if key == curses.KEY_UP:
                self.y -= 1
                self.y = max(0, self.y)
                continue
            if key == curses.KEY_DOWN:
                self.y += 1
                self.y = min(self.main_window_height - 1, self.y)
                continue
            if key == curses.KEY_LEFT:
                self.x -= 1
                self.x = max(0, self.x)
                continue
            if key == curses.KEY_RIGHT:
                self.x += 1
                self.x = min(self.main_window_width - 1, self.x)
                continue

            char = chr(key)
            if char == 'q':
                break

            if char == 's':
                return

            if char == 'w':
                self.grid.save("simu.lation")
                self.status_bar.show_message("Saved")
                continue

            symbol = self.grid.get(self.x, self.y)

            if char == ' ':
                new_symbol = symbol.next_symbol()

            elif char == 'd':
                new_symbol = Empty.from_symbol(symbol)

            else:
                try:
                    new_symbol = get_component(char)(symbol.up, symbol.left, symbol.right, symbol.down)
                except KeyError:
                    continue

            new_symbol = Symbol()
            self.grid.set(self.x, self.y, new_symbol)

    def simulate(self):
        self.status_bar.show_message("Simulation mode")

        self.stdscr.nodelay(1)
        for row in self.grid.grid:
            for symbol in row:
                symbol.reset()

        while 1:
            for row in self.grid.grid:
                for symbol in row:
                    symbol.calculate_new_state()

            time.sleep(0.1)

            for _y in range(self.main_window_height - 1):
                for _x in range(self.main_window_width - 1):
                    s = self.grid.grid[_y][_x]
                    s.switch_to_new_state()
                    if s.state.power:
                        highlight = curses.A_STANDOUT
                    else:
                        highlight = curses.A_NORMAL
                    self.stdscr.addstr(_y, _x, str(s), highlight)

            char = self.stdscr.getch()
            if char == -1:
                continue
            if chr(char) == 'q':
                break
            if chr(char) == ' ':
                for row in self.grid.grid:
                    for symbol in row:
                        if isinstance(symbol, Button):
                            symbol.pressed = not symbol.pressed

            self.stdscr.refresh()
        self.stdscr.nodelay(0)
