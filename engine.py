import curses
import time
from components import *


class SimulationEngine:
    x = 0
    y = 0

    def __init__(self, stdscr, grid):
        self.stdscr = stdscr
        self.grid = grid

    def edit_mode(self):
        while 1:
            for _y in range(curses.LINES - 1):
                for _x in range(curses.COLS - 1):
                    s = self.grid.grid[_y][_x]
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
                self.y = min(curses.LINES - 1, self.y)
                continue
            if key == curses.KEY_LEFT:
                self.x -= 1
                self.x = max(0, self.x)
                continue
            if key == curses.KEY_RIGHT:
                self.x += 1
                self.x = min(curses.COLS - 1, self.x)
                continue

            char = chr(key)
            if char == 'q':
                break

            if char == 's':
                self.simulate()
                continue

            if char == 'w':
                self.grid.save("simu.lation")
                continue

            symbol = self.grid.grid[self.y][self.x]

            if char == ' ':
                new_symbol = symbol.next_symbol()

            elif char == 'd':
                new_symbol = Empty.from_symbol(symbol)

            else:
                try:
                    new_symbol = get_component(char).from_symbol(symbol)
                except KeyError:
                    continue

            self.grid.grid[self.y][self.x] = new_symbol

    def simulate(self):
        self.stdscr.nodelay(1)
        for row in self.grid.grid:
            for symbol in row:
                symbol.reset()

        while 1:
            for row in self.grid.grid:
                for symbol in row:
                    symbol.calculate_new_state()

            time.sleep(0.1)

            for _y in range(curses.LINES - 1):
                for _x in range(curses.COLS - 1):
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
