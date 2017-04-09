import curses
from curses import wrapper
from components import *

import time


def simulate(stdscr, circuits):
    stdscr.nodelay(1)
    for row in circuits:
        for symbol in row:
            symbol.reset()

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
        if chr(char) == ' ':
            for row in circuits:
                for symbol in row:
                    if isinstance(symbol, Button):
                        symbol.pressed = not symbol.pressed

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

        if chr(key) == 'n':
            symbol = circuits[y][x]
            circuits[y][x] = Button.from_symbol(symbol)

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
