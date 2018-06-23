#include <boost/python.hpp>
#include <memory>
#include "symbol.h"
#include "battery.h"
#include "simulationengine.h"
#include "verticalline.h"


BOOST_PYTHON_MODULE (simulink) {
    using namespace boost::python;
    class_<Symbol, std::shared_ptr<Symbol>>("Symbol", init<std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>, std::shared_ptr<Symbol>>())
            .def(init<>())
            .def("__repr__", &Symbol::repr)
            .def("__str__", &Symbol::repr)
            .def("char", &Symbol::getChar)
            .def_readwrite("up", &Symbol::up)
            .def_readwrite("left", &Symbol::left)
            .def_readwrite("right", &Symbol::right)
            .def_readwrite("down", &Symbol::down)
            .def_readwrite("state", &Symbol::state)
            .def("build", build<Symbol>)
            .def("build_with_neighbours", build_with_neighbours<Symbol>)
            .def("build_from_existing", build_from_existing<Symbol>);
    class_<Battery, std::shared_ptr<Battery>, bases<Symbol>>("Battery", no_init)
            .def("build", build<Battery>)
            .def("build_with_neighbours", build_with_neighbours<Battery>)
            .def("build_from_existing", build_from_existing<Battery>);
    class_<VerticalLine, std::shared_ptr<VerticalLine>, bases<Symbol>>("VerticalLine", no_init)
            .def("build", build<VerticalLine>)
            .def("build_with_neighbours", build_with_neighbours<VerticalLine>)
            .def("build_from_existing", build_from_existing<VerticalLine>);
    class_<SimulationEngine>("SimulationEngine")
            .def("tick", &SimulationEngine::tick)
            .def("set_grid", &SimulationEngine::setGrid)
            .def("get_grid", &SimulationEngine::getGrid);
    class_<Grid>("Grid", init<int, int>())
            .def("get", &Grid::get)
            .def("set", &Grid::set);
    enum_<State>("ComponentState")
            .value("unpowered", unpowered)
            .value("powered", powered);
}
