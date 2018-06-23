//
// Created by t3mu on 23/06/18.
//

#include "line.h"

void Line::simulate() {
}

Line::Line() {
    state = unpowered;
    next_state = unpowered;
}

Line::Line(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                 std::shared_ptr<Symbol> d) : Symbol(u, l, r, d) {
    state = unpowered;
    next_state = unpowered;
}

