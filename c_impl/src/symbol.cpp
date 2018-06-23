#include "symbol.h"

Symbol::Symbol(std::shared_ptr<Symbol> u,
               std::shared_ptr<Symbol> l,
               std::shared_ptr<Symbol> r,
               std::shared_ptr<Symbol> d) {
    state = unpowered;
    next_state = unpowered;

    up = u;
    left = l;
    right = r;
    down = d;
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
