//
// Created by t3mu on 23/06/18.
//

#include "crossline.h"

std::string CrossLine::repr() const {
    return "+ " + std::to_string(this->state);
}

std::string CrossLine::getChar() {
    return "+";
}

CrossLine::CrossLine() {
    inputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
    outputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
}

CrossLine::CrossLine(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                           std::shared_ptr<Symbol> d) : Line(u, l, r, d) {
    inputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
    outputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
}
