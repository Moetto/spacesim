//
// Created by t3mu on 24/06/18.
//

#include "notport.h"

std::string NotPort::repr() const {
    return "i " + std::to_string(this->state);
}

std::string NotPort::getChar() {
    return "i";
}

NotPort::NotPort() {
    inputs = std::set<Direction>({UP});
    outputs = std::set<Direction>({DOWN});
    is_power_source = true;
}

bool NotPort::isPowered() {
    return !getsPowerFrom(UP);
}

void NotPort::simulate() {
    if (simulated)
        return;
    simulated = true;

    if (isPowered())
        next_state = unpowered;
    else
        next_state = powered;

    get_neighbour(DOWN)->simulate();
}

