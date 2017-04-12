#ifndef GRID_H
#define GRID_H
#include "symbol.h"

class Grid {
public:
    Grid(int width, int height);

    Symbol get_item(int x, int y);
};

#endif
