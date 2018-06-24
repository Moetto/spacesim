//
// Created by t3mu on 24/06/18.
//

#include "horizontalline.h"

std::string HorizontalLine::repr() const {
    return "- " + std::to_string(this->state);
}

std::string HorizontalLine::getChar() {
    return "-";
}

HorizontalLine::HorizontalLine() {
    inputs = std::set<Direction>({LEFT, RIGHT});
    outputs = std::set<Direction>({LEFT, RIGHT});
}

HorizontalLine::HorizontalLine(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                           std::shared_ptr<Symbol> d) : Line(u, l, r, d) {
    inputs = std::set<Direction>({LEFT, RIGHT});
    outputs = std::set<Direction>({LEFT, RIGHT});
}
