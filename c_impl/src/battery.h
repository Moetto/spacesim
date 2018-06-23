//
// Created by t3mu on 22/06/18.
//

#ifndef SIMULINK_BATTERY_H
#define SIMULINK_BATTERY_H

#include "symbol.h"

class Battery : public Symbol {
public:
    using Symbol::Symbol;

    std::string repr() const override ;
};


#endif //SIMULINK_BATTERY_H
