//
// Created by t3mu on 22/06/18.
//

#include "battery.h"

std::string Battery::repr() const {
    return "B " + std::to_string(this->state);
}

void Battery::simulate() {
}

Battery::Battery() {
    state = powered;
    next_state = powered;
}

Battery::Battery(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                 std::shared_ptr<Symbol> d) : Symbol(u, l, r, d) {
    state = powered;
    next_state = powered;
}

std::string Battery::getChar() {
    return "B";
}
