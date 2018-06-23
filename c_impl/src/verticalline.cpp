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
