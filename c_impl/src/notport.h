//
// Created by t3mu on 24/06/18.
//

#ifndef SIMULINK_NOTPORT_H
#define SIMULINK_NOTPORT_H


#include <string>
#include "symbol.h"

class NotPort : public Symbol {
public:
    NotPort();

    std::string repr() const override;

    std::string getChar() override;

    bool isPowered() override;

    void simulate() override;
};


#endif //SIMULINK_NOTPORT_H
