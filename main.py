import curses
import argparse
from curses import wrapper
from engine import SimulationEngine

from grid import Grid


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    if params.filename:
        grid = Grid.load(params.filename, curses.COLS, curses.LINES)
    else:
        grid = Grid(curses.COLS, curses.LINES)

    engine = SimulationEngine(stdscr, grid)
    engine.edit_mode()


args = argparse.ArgumentParser()
args.add_argument("-l", "--load", dest="filename", default=None)
params = args.parse_args()

wrapper(main)
