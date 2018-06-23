
#include "grid.h"
#include "battery.h"
#include <memory>

Grid::Grid(unsigned int w, unsigned int h) {
    symbols = std::vector<std::shared_ptr<Symbol>>(w * h, std::make_shared<Symbol>());
    width = w;
    height = h;
}

std::shared_ptr<Symbol> Grid::get(unsigned int x, unsigned int y) {
    return symbols[y * width + x];
}

void Grid::set(unsigned int x, unsigned int y, std::shared_ptr<Symbol> &s) {
    symbols[y * width +x] = s;
}
