import curses
import argparse
from curses import wrapper
from time import sleep

from build.simulink import *

from controller import Input, get_input
from screen import Screen
from state import State


def setup_test(grid):
    a = grid.get(1, 1)
    # b = Battery.build_from_existing(a)
    b = Battery.build()
    grid.set(1, 1, b)
    for i in range(2, 6):
        b = VerticalLine.build()
        grid.set(1, i, b)

    b = CrossLine.build()
    grid.set(1, 4, b)

    b = HorizontalLine.build()
    grid.set(2, 1, b)

    b = VerticalLine.build()
    grid.set(3, 1, b)

    for y in range(2, 8):
        for x in [4, 6]:
            b = VerticalLine.build()
            grid.set(x, y, b)


    b = NotPort.build()
    grid.set(4, 2, b)

    b = NotPort.build()
    grid.set(6, 4, b)

    b = Battery.build()
    grid.set(6, 2, b)


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    if params.filename:
        grid = Grid.load(params.filename, curses.COLS, curses.LINES)
    else:
        grid = Grid(curses.COLS, curses.LINES)

    engine = SimulationEngine()
    engine.set_grid(grid)

    screen = Screen(stdscr, grid)
    state = State("Edit mode", False, 0, 0, 0, 0)
    screen.draw(state)

    inp = get_input(stdscr)

    setup_test(grid)

    while inp != Input.QUIT:
        if inp == Input.SIMULATE:
            state.message = "Simulation"
            state.show_power = True
            stdscr.nodelay(True)
            inp = get_input(stdscr)
            while inp != Input.QUIT:
                engine.tick()
                screen.draw(state)
                sleep(.55)
                inp = get_input(stdscr)
            state.message = "Edit mode"
            state.show_power = False
            stdscr.nodelay(False)
        if inp == Input.UP:
            state.cursor_y -= 1
        if inp == Input.DOWN:
            state.cursor_y += 1
        if inp == Input.LEFT:
            state.cursor_x -= 1
        if inp == Input.RIGHT:
            state.cursor_x += 1

        new = None
        if inp == Input.BATTERY:
            new = Battery.build()
        elif inp == Input.VERTICAL_LINE:
            new = VerticalLine.build()
        elif inp == Input.HORIZONTAL_LINE:
            new = HorizontalLine.build()
        elif inp == Input.CROSS_LINE:
            new = CrossLine.build()
        elif inp == Input.NOT_PORT:
            new = NotPort.build()
        elif inp == Input.CLEAR:
            new = Empty.build()
        if new:
            grid.set(state.cursor_x, state.cursor_y, new)

        screen.draw(state)
        inp = get_input(stdscr)


args = argparse.ArgumentParser()
args.add_argument("-l", "--load", dest="filename", default=None)
params = args.parse_args()

wrapper(main)
