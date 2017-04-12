//
// Created by moetto on 12/04/17.
//

#ifndef SIMULINK_SIMULATIONENGINE_H
#define SIMULINK_SIMULATIONENGINE_H

#include <vector>
#include "symbol.h"

class SimulationEngine {
    std::vector<std::vector<Symbol *> *> components;

public:
    SimulationEngine();

    void tick();

    Symbol get_item(unsigned long x, unsigned long y);
};


#endif //SIMULINK_SIMULATIONENGINE_H
