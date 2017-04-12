#ifndef SYMBOL_H
#define SYMBOL_H

#include <string>
#include "state.h"

class Symbol {
    State state;
    State next_state;

public:
    Symbol();

    std::string repr();

    void simulate();

    void switch_state();

};

#endif