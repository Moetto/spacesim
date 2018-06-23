#include "symbol.h"

Symbol::Symbol(std::shared_ptr<Symbol> n,
               std::shared_ptr<Symbol> e,
               std::shared_ptr<Symbol> w,
               std::shared_ptr<Symbol> s) {
    state = unpowered;
    next_state = unpowered;

    north = n;
    west = w;
    east = e;
    south = s;
}

Symbol::Symbol() {
    state = unpowered;
    next_state = unpowered;
}

void Symbol::simulate() {
    if (state == powered) {
        next_state = unpowered;
    } else {
        next_state = powered;
    }
}

void Symbol::switchState() {
    state = next_state;
}

std::string Symbol::repr() const {
    return "E " + std::to_string(this->state);
}

std::ostream &operator<<(std::ostream &strm, Symbol s) {
    strm << (&s)->repr() << " " << s.state;
    return strm;
}
