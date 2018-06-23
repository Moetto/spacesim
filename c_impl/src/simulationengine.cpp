//
// Created by moetto on 12/04/17.
//

#include "simulationengine.h"
#include <utility>

SimulationEngine::SimulationEngine() = default;

void SimulationEngine::tick() {
    for (auto &symbol : grid->symbols) {
        symbol->simulate();
    }

    for (auto &symbol : grid->symbols) {
        symbol->switchState();
    }
}

std::shared_ptr<Grid> SimulationEngine::getGrid() {
    return grid;
}

void SimulationEngine::setGrid(std::shared_ptr<Grid> grid) {
    this->grid = std::move(grid);
}
