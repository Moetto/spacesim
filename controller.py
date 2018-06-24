import curses
from enum import Enum, auto


class Input(Enum):
    EMPTY = auto()
    QUIT = auto()
    SIMULATE = auto()
    SAVE = auto()
    UP = auto()
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()
    CLEAR = auto()
    NEXT_SYMBOL = auto()
    BATTERY = auto()
    VERTICAL_LINE = auto()
    HORIZONTAL_LINE = auto()
    CROSS_LINE = auto()
    NOT_PORT = auto()


def symbol_for_char(char):
    if char == "|" or char == "I":
        return Input.VERTICAL_LINE
    if char == "-":
        return Input.HORIZONTAL_LINE
    if char == "+":
        return Input.CROSS_LINE
    if char == "B":
        return Input.BATTERY
    if char == "i":
        return Input.NOT_PORT
    return Input.EMPTY


def get_input(stdscr) -> Input:
    key = stdscr.getch()

    if key == curses.ERR:
        return Input.EMPTY

    # Cursor movement
    if key == curses.KEY_UP:
        return Input.UP
    if key == curses.KEY_DOWN:
        return Input.DOWN
    if key == curses.KEY_LEFT:
        return Input.LEFT
    if key == curses.KEY_RIGHT:
        return Input.RIGHT
    char = chr(key)
    if char == 'q':
        return Input.QUIT
    if char == 's':
        return Input.SIMULATE
    if char == 'w':
        return Input.SAVE
    if char == ' ':
        return Input.NEXT_SYMBOL
    if char == 'd':
        return Input.CLEAR
    else:
        return symbol_for_char(char)
