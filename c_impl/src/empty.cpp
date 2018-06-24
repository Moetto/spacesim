//
// Created by t3mu on 23/06/18.
//

#include "empty.h"

std::string Empty::repr() const {
    return "E " + std::to_string(this->state);
}

std::string Empty::getChar() {
    return " ";
}

Empty::Empty() {
    inputs = std::set<Direction>();
    outputs = std::set<Direction>();

    state = unpowered;
    next_state = unknown;
    is_power_source = false;
}

Empty::Empty(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                           std::shared_ptr<Symbol> d) : Symbol(u, l, r, d) {
    inputs = std::set<Direction>();
    outputs = std::set<Direction>();

    state = unpowered;
    next_state = unknown;
    is_power_source = false;
}

void Empty::simulate() {
}

bool Empty::isPowered() {
    return false;
}

