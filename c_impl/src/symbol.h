#ifndef SYMBOL_H
#define SYMBOL_H

#include <string>
#include <iostream>
#include <memory>
#include <boost/shared_ptr.hpp>
#include "state.h"

class Symbol {
public:
    std::shared_ptr<Symbol> up, left, right, down;
    State state, next_state;

    Symbol();

    Symbol(std::shared_ptr<Symbol> u,
           std::shared_ptr<Symbol> r,
           std::shared_ptr<Symbol> l,
           std::shared_ptr<Symbol> d);

    virtual void simulate();

    void switchState();

    virtual std::string repr() const;
};

std::ostream &operator<<(std::ostream &, Symbol);

template<class T>
std::shared_ptr<Symbol> build() {
    return std::shared_ptr<Symbol>(new T());
}

template<class T>
std::shared_ptr<Symbol>
build_with_neighbours(std::shared_ptr<Symbol> s1, std::shared_ptr<Symbol> s2, std::shared_ptr<Symbol> s3, std::shared_ptr<Symbol> s4) {
    return std::shared_ptr<Symbol>(new T(s1, s2, s3, s4));
}


#endif