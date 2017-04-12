//
// Created by moetto on 12/04/17.
//

#include "simulationengine.h"

SimulationEngine::SimulationEngine() {

}

void SimulationEngine::tick() {
    for (auto row_it = components.begin(); row_it != components.end(); row_it++) {
        for (auto comp_it = (*row_it)->begin(); comp_it != (*row_it)->end(); comp_it++) {
            (*comp_it)->simulate();
        }
    }
    for (auto row_it = components.begin(); row_it != components.end(); row_it++) {
        for (auto comp_it = (*row_it)->begin(); comp_it != (*row_it)->end(); comp_it++) {
            (*comp_it)->switch_state();
        }
    }
}

Symbol SimulationEngine::get_item(unsigned long x, unsigned long y) {
    return *(*components.at(y)).at(x);
}
