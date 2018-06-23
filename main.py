import curses
import argparse
from curses import wrapper
from time import sleep

from build.simulink import *

from controller import Input, get_input
from screen import Screen
from state import State


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

    while inp != Input.QUIT:
        if inp == Input.SIMULATE:
            state.message = "Simulation"
            state.show_power = True
            stdscr.nodelay(True)
            inp = get_input(stdscr)
            while inp != Input.QUIT:
                engine.tick()
                screen.draw(state)
                sleep(.05)
                inp = get_input(stdscr)
            stdscr.nodelay(False)
            state.message = "Edit mode"
            state.show_power = False
        if inp == Input.UP:
            state.cursor_y -= 1
        if inp == Input.DOWN:
            state.cursor_y += 1
        if inp == Input.LEFT:
            state.cursor_x -= 1
        if inp == Input.RIGHT:
            state.cursor_x += 1
        if inp == Input.BATTERY or inp == Input.VERTICAL_LINE or inp == Input.NEXT_SYMBOL or inp == Input.CLEAR or inp == Input.EMPTY:
            current = grid.get(state.cursor_x, state.cursor_y)
            new = None
            if inp == Input.BATTERY:
                new = Battery.build_from_existing(current)
            elif inp == Input.VERTICAL_LINE:
                new = VerticalLine.build_from_existing(current)
            if new:
                grid.set(state.cursor_x, state.cursor_y, new)

        screen.draw(state)
        sleep(0.1)
        inp = get_input(stdscr)


args = argparse.ArgumentParser()
args.add_argument("-l", "--load", dest="filename", default=None)
params = args.parse_args()

wrapper(main)
