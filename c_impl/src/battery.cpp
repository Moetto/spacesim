//
// Created by t3mu on 22/06/18.
//

#include "battery.h"

std::string Battery::repr() const {
    return "B " + std::to_string(this->state);
}
