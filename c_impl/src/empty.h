//
// Created by t3mu on 23/06/18.
//

#ifndef SIMULINK_EMPTY_H
#define SIMULINK_EMPTY_H

#include "symbol.h"


class Empty : public Symbol {
public:
    Empty();

    Empty(std::shared_ptr<Symbol> u,
          std::shared_ptr<Symbol> l,
          std::shared_ptr<Symbol> r,
          std::shared_ptr<Symbol> d);

    std::string repr() const override;

    std::string getChar() override;

    void simulate() override ;

    bool isPowered() override ;
};


#endif //SIMULINK_EMPTY_H
