import curses
import argparse
from curses import wrapper
from build.simulink import SimulationEngine, Grid

from editor import Editor


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    if params.filename:
        grid = Grid.load(params.filename, curses.COLS, curses.LINES)
    else:
        grid = Grid(curses.COLS, curses.LINES)

    engine = SimulationEngine()
    engine.set_grid(grid)

    editor = Editor(stdscr, grid)
    while 1:
        editor.edit_mode()
        engine.tick()


args = argparse.ArgumentParser()
args.add_argument("-l", "--load", dest="filename", default=None)
params = args.parse_args()

wrapper(main)
