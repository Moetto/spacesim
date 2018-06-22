//
// Created by moetto on 12/04/17.
//

#ifndef SIMULINK_SIMULATIONENGINE_H
#define SIMULINK_SIMULATIONENGINE_H

#include <vector>
#include <memory>
#include "symbol.h"
#include "grid.h"

class SimulationEngine {
    std::shared_ptr<Grid> grid;

public:
    SimulationEngine();

    void tick();

    void setGrid(std::shared_ptr<Grid> grid);

    std::shared_ptr<Grid> getGrid();
};


#endif //SIMULINK_SIMULATIONENGINE_H
