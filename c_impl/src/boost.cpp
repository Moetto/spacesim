#include <boost/python.hpp>
#include <memory>
#include "symbol.h"
#include "simulationengine.h"


BOOST_PYTHON_MODULE (simulink) {
    using namespace boost::python;
    class_<Symbol, std::shared_ptr<Symbol>>("Symbol", init<std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>>())
            .def(init<>())
            .def(self_ns::str(self_ns::self))
            .def("simulate", &Symbol::simulate)
            .def("switch_state", &Symbol::switchState);
    class_<SimulationEngine>("SimulationEngine")
            .def("tick", &SimulationEngine::tick)
            .def("set_grid", &SimulationEngine::setGrid)
            .def("get_grid", &SimulationEngine::getGrid);
    class_<Grid>("Grid", init<int, int>())
            .def("get", &Grid::get)
            .def("set", &Grid::set);
}
