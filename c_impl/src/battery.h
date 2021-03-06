//
// Created by t3mu on 22/06/18.
//

#ifndef SIMULINK_BATTERY_H
#define SIMULINK_BATTERY_H

#include "symbol.h"

class Battery : public Symbol {
public:
    Battery();

    Battery(std::shared_ptr<Symbol> u,
            std::shared_ptr<Symbol> l,
            std::shared_ptr<Symbol> r,
            std::shared_ptr<Symbol> d);

    bool isPowered() override;

    std::string repr() const override;

    std::string getChar() override;
};


#endif //SIMULINK_BATTERY_H
