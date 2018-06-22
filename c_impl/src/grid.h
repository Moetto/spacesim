#ifndef GRID_H
#define GRID_H

#include <vector>
#include "symbol.h"

class Grid {
    std::vector<std::shared_ptr<Symbol>> symbols;
    unsigned int width, height;

public:
    Grid(unsigned int w, unsigned int h);

    std::shared_ptr<Symbol> get(unsigned int x, unsigned int y);

    void set(unsigned int x, unsigned int y, std::shared_ptr<Symbol> &s);
};
#endif
