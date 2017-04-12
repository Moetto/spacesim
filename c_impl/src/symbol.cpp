#include "symbol.h"

Symbol::Symbol() {

}

std::string Symbol::repr() {
    return "S";
}

void Symbol::simulate() {
    next_state = State();
}

void Symbol::switch_state() {
    state = next_state;
    next_state = NULL;
}
