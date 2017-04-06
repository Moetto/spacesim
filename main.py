import curses
from curses import wrapper


class Symbol:
    char = None
    power = False

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

    def set_power(self, on):
        self.power = on

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
        return Line.from_symbol(self)

    @classmethod
    def get_empty(cls):
        return Empty(None, None, None, None)

    def set_power(self, on):
        pass


class Line(Symbol):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '-'

    def next_symbol(self):
        return Cross.from_symbol(self)

    def set_power(self, on):
        if on == self.power:
            return
        super().set_power(on)
        for s in self.left, self.right:
            s.set_power(on)


class Cross(Symbol):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '+'

    def next_symbol(self):
        return Battery.from_symbol(self)

    def set_power(self, on):
        if on == self.power:
            return
        super().set_power(on)
        for s in self.left, self.right, self.up, self.down:
            s.set_power(on)


class Battery(Symbol):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'B'

    def next_symbol(self):
        return Engine.from_symbol(self)

    def set_power(self, on):
        if on == self.power:
            return
        super().set_power(on)
        for s in self.left, self.right, self.up, self.down:
            s.set_power(on)


class Engine(Symbol):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'E'

    def next_symbol(self):
        return Empty.from_symbol(self)


def simulate(circuits):
    batteries = []
    for y in range(len(circuits) - 1):
        row = circuits[y]
        for symbol in row:
            if type(symbol) == Battery:
                batteries.append(symbol)

    for battery in batteries:
        battery.set_power(True)


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
            circuits[y][x] = Line.from_symbol(symbol)

        if chr(key) == '+':
            symbol = circuits[y][x]
            circuits[y][x] = Cross.from_symbol(symbol)

        if chr(key) == 'e':
            symbol = circuits[y][x]
            circuits[y][x] = Engine.from_symbol(symbol)

        if chr(key) == 'q':
            break

        if chr(key) == 's':
            simulate(circuits)

        for _y in range(curses.LINES - 1):
            for _x in range(curses.COLS - 1):
                s = circuits[_y][_x]
                if s.power:
                    highlight = curses.A_STANDOUT
                else:
                    highlight = curses.A_NORMAL
                s.power = False
                stdscr.addstr(_y, _x, str(s), highlight)
        stdscr.refresh()
        stdscr.move(y, x)


wrapper(main)
