#include <boost/python.hpp>
#include "symbol.h"
#include "simulationengine.h"
#include "gamestate.h"


BOOST_PYTHON_MODULE (simulink) {
    using namespace boost::python;
    class_<Symbol>("Symbol")
            .def("__repr__", &Symbol::repr);
    class_<SimulationEngine>("SimulationEngine")
            .def("get_item", &SimulationEngine::get_item)
            .def("tick", &SimulationEngine::tick);
    class_<GameState>("GameState");
}
