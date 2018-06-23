import curses

from build.simulink import *

from state import State


class Screen:
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
        self.status_bar = Screen.StatusBar(self.main_window_height, 0, 3, self.main_window_width)
        stdscr.resize(self.main_window_height, self.main_window_width)
        self.grid = grid
        self.last_shown_msg = None

    def draw(self, state: State):
        if state.message != self.last_shown_msg:
            self.status_bar.show_message(state.message)
            self.last_shown_msg = state.message
        for _y in range(self.main_window_height - 1):
            for _x in range(self.main_window_width - 1):
                s = self.grid.get(_x, _y)
                if state.show_power and s.state == ComponentState.powered:
                    hilight = curses.A_STANDOUT
                else:
                    hilight = curses.A_NORMAL
                self.stdscr.addstr(_y, _x, s.char(), hilight)
        self.stdscr.move(state.cursor_y, state.cursor_x)

    """
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
        """
