import curses
from curses import wrapper

import time
from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @staticmethod
    def get_opposite_direction(direction):
        if direction == Direction.UP:
            return Direction.DOWN
        if direction == Direction.DOWN:
            return Direction.UP
        if direction == Direction.LEFT:
            return Direction.RIGHT
        if direction == Direction.RIGHT:
            return Direction.LEFT


class State:
    def __init__(self, power=False):
        self.power = power


class Port:
    pass


class Blocked(Port):
    pass


class Input(Port):
    pass


class Output(Port):
    pass


class InputOutput(Input, Output):
    pass


class Symbol:
    char = None
    state = State()
    new_state = State()
    up_port = Blocked()
    down_port = Blocked()
    left_port = Blocked()
    right_port = Blocked()

    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __str__(self):
        return self.char

    def __repr__(self):
        return self.char

    def next_symbol(self):
        raise NotImplementedError

    def get_port(self, direction):
        if direction == Direction.UP:
            return self.up_port
        if direction == Direction.DOWN:
            return self.down_port
        if direction == Direction.LEFT:
            return self.left_port
        if direction == Direction.RIGHT:
            return self.right_port

    def _get_neighbouring_symbol(self, direction):
        if direction == Direction.UP:
            return self.up
        if direction == Direction.DOWN:
            return self.down
        if direction == Direction.LEFT:
            return self.left
        if direction == Direction.RIGHT:
            return self.right

    def _is_powered_from(self, direction):
        neighbour = self._get_neighbouring_symbol(direction)
        neighbour_port = neighbour.get_port(Direction.get_opposite_direction(direction))
        if neighbour.state.power and isinstance(self.get_port(direction), Input) and isinstance(neighbour_port, Output):
            return True
        return False

    def calculate_new_state(self):
        self.new_state = State()
        for direction in Direction:
            if self._is_powered_from(direction):
                self.new_state = State(True)
                return

    def switch_to_new_state(self):
        self.state = self.new_state
        self.new_state = None

    @classmethod
    def from_symbol(cls, symbol):
        s = cls(symbol.up, symbol.down, symbol.left, symbol.right)
        s.up.down = s
        s.down.up = s
        s.left.right = s
        s.right.left = s
        return s


class Empty(Symbol):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = ' '

    def next_symbol(self):
        return HorizontalLine.from_symbol(self)

    @classmethod
    def get_empty(cls):
        return Empty(None, None, None, None)


class HorizontalLine(Symbol):
    left_port = InputOutput()
    right_port = InputOutput()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '-'

    def next_symbol(self):
        return VerticalLine.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()
        if self._is_powered_from(Direction.LEFT) or self._is_powered_from(Direction.RIGHT):
            self.new_state = State(True)


class VerticalLine(Symbol):
    up_port = InputOutput()
    down_port = InputOutput()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '|'

    def next_symbol(self):
        return Cross.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()
        if self._is_powered_from(Direction.UP) or self._is_powered_from(Direction.DOWN):
            self.new_state = State(True)


class Cross(Symbol):
    left_port = InputOutput()
    right_port = InputOutput()
    up_port = InputOutput()
    down_port = InputOutput()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '+'

    def next_symbol(self):
        return Battery.from_symbol(self)


class Battery(Symbol):
    up_port = Output()
    down_port = Output()
    left_port = Output()
    right_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'B'

    def next_symbol(self):
        return Engine.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State(True)


class Engine(Symbol):
    up_port = Input()
    down_port = Input()
    left_port = Input()
    right_port = Input()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'E'

    def next_symbol(self):
        return PortAnd.from_symbol(self)


class PortAnd(Symbol):
    left_port = Input()
    right_port = Input()
    down_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'T'

    def next_symbol(self):
        return PortOr.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()
        if self._is_powered_from(Direction.LEFT) and self._is_powered_from(Direction.RIGHT):
            self.new_state = State(True)


class PortOr(Symbol):
    left_port = Input()
    right_port = Input()
    down_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'Y'

    def next_symbol(self):
        return PortNot.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()
        if self._is_powered_from(Direction.LEFT) or self._is_powered_from(Direction.RIGHT):
            self.new_state = State(True)


class PortNot(Symbol):
    up_port = Input()
    down_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'i'

    def next_symbol(self):
        return Empty.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State(True)
        if self._is_powered_from(Direction.UP):
            self.new_state = State()


def simulate(stdscr, circuits):
    stdscr.nodelay(1)
    for row in circuits:
        for symbol in row:
            symbol.state = State()
            symbol.new_state = State()

    while 1:
        for row in circuits:
            for symbol in row:
                symbol.calculate_new_state()

        time.sleep(0.1)

        for _y in range(curses.LINES - 1):
            for _x in range(curses.COLS - 1):
                s = circuits[_y][_x]
                s.switch_to_new_state()
                if s.state.power:
                    highlight = curses.A_STANDOUT
                else:
                    highlight = curses.A_NORMAL
                stdscr.addstr(_y, _x, str(s), highlight)

        char = stdscr.getch()
        if char == -1:
            continue
        if chr(char) == 'q':
            break

        stdscr.refresh()
    stdscr.nodelay(0)


def main(stdscr):
    x = 0
    y = 0
    stdscr.clear()
    stdscr.refresh()
    circuits = []
    for _y in range(curses.LINES - 1):
        row = []
        for _x in range(curses.COLS - 1):
            row.append(Empty.get_empty())
        circuits.append(row)

    for _y in range(curses.LINES - 1):
        for _x in range(curses.COLS - 1):
            s = circuits[_y][_x]
            row = circuits[_y]

            if _x > 0:
                left = row[_x - 1]
            else:
                left = Empty.get_empty()
            left.right = s
            s.left = left

            if _x < curses.COLS - 2:
                right = row[_x + 1]
            else:
                right = Empty.get_empty()
            right.left = s
            s.right = right

            if _y > 0:
                up = circuits[_y - 1][_x]
            else:
                up = Empty.get_empty()

            up.down = s
            s.up = up

            if _y < curses.LINES - 2:
                down = circuits[_y + 1][_x]
            else:
                down = Empty.get_empty()
            down.up = s
            s.down = down

    while 1:
        key = stdscr.getch()

        # Cursor movement
        if key == curses.KEY_UP:
            y -= 1
            y = max(0, y)
        if key == curses.KEY_DOWN:
            y += 1
            y = min(curses.LINES - 1, y)
        if key == curses.KEY_LEFT:
            x -= 1
            x = max(0, x)
        if key == curses.KEY_RIGHT:
            x += 1
            x = min(curses.COLS - 1, x)

        # Mark char
        if chr(key) == ' ':
            old = circuits[y][x]
            new_symbol = old.next_symbol()
            circuits[y][x] = new_symbol

        if chr(key) == 'd':
            symbol = circuits[y][x]
            symbol = Empty.from_symbol(symbol)
            circuits[y][x] = symbol

        if chr(key) == 'b':
            symbol = circuits[y][x]
            circuits[y][x] = Battery.from_symbol(symbol)

        if chr(key) == '-':
            symbol = circuits[y][x]
            circuits[y][x] = HorizontalLine.from_symbol(symbol)

        if chr(key) == 'l':
            symbol = circuits[y][x]
            circuits[y][x] = VerticalLine.from_symbol(symbol)

        if chr(key) == '+':
            symbol = circuits[y][x]
            circuits[y][x] = Cross.from_symbol(symbol)

        if chr(key) == 'e':
            symbol = circuits[y][x]
            circuits[y][x] = Engine.from_symbol(symbol)

        if chr(key) == 't':
            symbol = circuits[y][x]
            circuits[y][x] = PortAnd.from_symbol(symbol)

        if chr(key) == 'y':
            symbol = circuits[y][x]
            circuits[y][x] = PortOr.from_symbol(symbol)

        if chr(key) == 'i':
            symbol = circuits[y][x]
            circuits[y][x] = PortNot.from_symbol(symbol)

        if chr(key) == 'q':
            break

        if chr(key) == 's':
            simulate(stdscr, circuits)

        for _y in range(curses.LINES - 1):
            for _x in range(curses.COLS - 1):
                s = circuits[_y][_x]
                stdscr.addstr(_y, _x, str(s))

        stdscr.move(y, x)


wrapper(main)
