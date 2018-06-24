//
// Created by t3mu on 22/06/18.
//

#include "battery.h"

std::string Battery::repr() const {
    return "B " + std::to_string(this->state);
}

Battery::Battery() {
    is_power_source = true;
    state = powered;
    next_state = unknown;
    inputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
    outputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
}

Battery::Battery(std::shared_ptr<Symbol> u, std::shared_ptr<Symbol> l, std::shared_ptr<Symbol> r,
                 std::shared_ptr<Symbol> d) : Symbol(u, l, r, d) {
    is_power_source = true;
    state = powered;
    next_state = unknown;
    inputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
    outputs = std::set<Direction>({UP, LEFT, RIGHT, DOWN});
}

std::string Battery::getChar() {
    return "B";
}

bool Battery::isPowered() {
    return true;
}

