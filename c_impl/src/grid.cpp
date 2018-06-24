
#include "grid.h"
#include "empty.h"
#include <memory>

Grid::Grid(unsigned int w, unsigned int h) {
    symbols = std::vector<std::shared_ptr<Symbol>>(w * h);
    width = w;
    height = h;
    link();
}

std::shared_ptr<Symbol> Grid::get(unsigned int x, unsigned int y) {
    return symbols[y * width + x];
}

void Grid::set(unsigned int x, unsigned int y, std::shared_ptr<Symbol> s) {
    symbols[y * width + x] = s;
    link(x, y);
}

void Grid::link(unsigned int x, unsigned int y) {
    auto s = get(x, y);
    std::shared_ptr<Symbol> other;
    if (x > 0) {
        other = get(x - 1, y);
    } else {
        other = build<Empty>();
    }
    s->left = other;
    other->right = s;

    if (x < width - 1) {
        other = get(x + 1, y);
    } else {
        other = build<Empty>();
    }
    s->right = other;
    other->left = s;

    if (y > 0) {
        other = get(x, y - 1);
    } else {
        other = build<Empty>();
    }
    s->up = other;
    other->down = s;

    if (y < height - 1) {
        other = get(x, y + 1);
    } else {
        other = build<Empty>();
    }
    s->down = other;
    other->up = s;
}

void Grid::link() {
    for (int i = 0; i < width * height; i++) {
        symbols[i] = build<Empty>();
    }
    for (unsigned int y = 0; y < height; y++) {
        for (unsigned int x = 0; x < width; x++) {
            link(x, y);
        }
    }
}
