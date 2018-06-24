//
// Created by t3mu on 23/06/18.
//

#ifndef SIMULINK_LINE_H
#define SIMULINK_LINE_H
#include "symbol.h"

class Line : public Symbol{
public:
    Line();

    Line(std::shared_ptr<Symbol> u,
            std::shared_ptr<Symbol> l,
            std::shared_ptr<Symbol> r,
            std::shared_ptr<Symbol> d);

    std::string repr() const override = 0;

    std::string getChar() override = 0;
};


#endif //SIMULINK_LINE_H
