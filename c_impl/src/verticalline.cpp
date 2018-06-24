//
// Created by t3mu on 23/06/18.
//

#include "verticalline.h"

std::string VerticalLine::repr() const {
    return "| " + std::to_string(this->state);
}

std::string VerticalLine::getChar() {
    return "|";
}

VerticalLine::VerticalLine() {
    inputs = std::set<Direction>({UP, DOWN});
    outputs = std::set<Direction>({UP, DOWN});
}

VerticalLine::VerticalLine(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                           std::shared_ptr<Symbol> d) : Line(u, l, r, d) {
    inputs = std::set<Direction>({UP, DOWN});
    outputs = std::set<Direction>({UP, DOWN});
}
