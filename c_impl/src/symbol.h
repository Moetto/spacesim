#ifndef SYMBOL_H
#define SYMBOL_H

#include <string>
#include <iostream>
#include <memory>
#include <boost/shared_ptr.hpp>
#include "state.h"

class Symbol {
public:
    std::shared_ptr<Symbol> north, west, east, south;
    State state, next_state;

    Symbol();

    Symbol(std::shared_ptr<Symbol> n,
           std::shared_ptr<Symbol> e,
           std::shared_ptr<Symbol> w,
           std::shared_ptr<Symbol> s);

    void simulate();

    void switchState();

    virtual std::string repr() const;
};

std::ostream &operator<<(std::ostream &, Symbol);

#endif