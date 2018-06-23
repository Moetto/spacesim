#include <boost/python.hpp>
#include <memory>
#include "symbol.h"
#include "battery.h"
#include "simulationengine.h"


BOOST_PYTHON_MODULE (simulink) {
    using namespace boost::python;
    class_<Symbol, std::shared_ptr<Symbol>>("Symbol", init<std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>>())
            .def(init<>())
            .def("__repr__", &Symbol::repr)
            .def("__str__", &Symbol::repr);
    class_<Battery, std::shared_ptr<Battery>>("Battery", init<std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>>())
            .def(init<>())
            .def("__repr__", &Battery::repr)
            .def("__str__", &Battery::repr);
    class_<SimulationEngine>("SimulationEngine")
            .def("tick", &SimulationEngine::tick)
            .def("set_grid", &SimulationEngine::setGrid)
            .def("get_grid", &SimulationEngine::getGrid);
    class_<Grid>("Grid", init<int, int>())
            .def("get", &Grid::get)
            .def("set", &Grid::set);
}
