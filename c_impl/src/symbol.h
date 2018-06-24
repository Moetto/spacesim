#ifndef SYMBOL_H
#define SYMBOL_H

#include <string>
#include <iostream>
#include <memory>
#include <boost/shared_ptr.hpp>
#include <vector>
#include <set>
#include "state.h"
#include "direction.h"

class Symbol {

public:
    bool is_power_source, simulated;

    std::set<Direction> inputs;
    std::set<Direction> outputs;

    std::shared_ptr<Symbol> up, left, right, down;
    State state, next_state;

    Symbol();

    Symbol(std::shared_ptr<Symbol> u,
           std::shared_ptr<Symbol> r,
           std::shared_ptr<Symbol> l,
           std::shared_ptr<Symbol> d);

    virtual void simulate();

    virtual void reset();

    void switchState();

    bool hasInputFrom(Direction d);

    bool hasOutputTo(Direction d);

    bool getsPowerFrom(Direction d);

    virtual bool isPowered();

    std::shared_ptr<Symbol> get_neighbour(Direction d);

    virtual std::string repr() const;

    virtual std::string getChar();

};

template<class T>
std::shared_ptr<Symbol> build() {
    return std::shared_ptr<Symbol>(new T());
}

template<class T>
std::shared_ptr<Symbol>
build_with_neighbours(std::shared_ptr<Symbol> up, std::shared_ptr<Symbol> left, std::shared_ptr<Symbol> right,
                      std::shared_ptr<Symbol> down) {
    auto t = std::shared_ptr<Symbol>(new T(up, left, right, down));
    /*
    up->down = t;
    left->right = t;
    right->left = t;
    down->up = t;
     */
    return t;
}

template<class T>
std::shared_ptr<Symbol>
build_from_existing(std::shared_ptr<Symbol> s) {
    std::shared_ptr<Symbol> up, left, right, down;
    up = s->up;
    left = s->left;
    right = s->right;
    down = s->down;
    auto new_s = std::shared_ptr<Symbol>(new T(up, left, right, down));
    /*
    up->down = new_s;
    left->right = new_s;
    right->left = new_s;
    down->up = new_s;
     */
    return new_s;
}

#endif