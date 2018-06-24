#include <boost/python.hpp>
#include <memory>
#include "symbol.h"
#include "battery.h"
#include "simulationengine.h"
#include "verticalline.h"
#include "horizontalline.h"
#include "crossline.h"
#include "empty.h"
#include "notport.h"


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
            .def("build", build<Symbol>);
    class_<Empty, std::shared_ptr<Empty>, bases<Symbol>>("Empty", no_init)
            .def("build", build<Empty>);
    class_<Battery, std::shared_ptr<Battery>, bases<Symbol>>("Battery", no_init)
            .def("build", build<Battery>);
    class_<VerticalLine, std::shared_ptr<VerticalLine>, bases<Symbol>>("VerticalLine", no_init)
            .def("build", build<VerticalLine>);
    class_<HorizontalLine, std::shared_ptr<HorizontalLine>, bases<Symbol>>("HorizontalLine", no_init)
            .def("build", build<HorizontalLine>);
    class_<CrossLine, std::shared_ptr<CrossLine>, bases<Symbol>>("CrossLine", no_init)
            .def("build", build<CrossLine>);
    class_<NotPort, std::shared_ptr<NotPort>, bases<Symbol>>("NotPort", no_init)
            .def("build", build<NotPort>);
    class_<SimulationEngine>("SimulationEngine")
            .def("tick", &SimulationEngine::tick)
            .def("set_grid", &SimulationEngine::setGrid)
            .def("get_grid", &SimulationEngine::getGrid);
    class_<Grid>("Grid", init<int, int>())
            .def("get", &Grid::get)
            .def("set", &Grid::set);
    enum_<State>("ComponentState")
            .value("unknown", unknown)
            .value("unpowered", unpowered)
            .value("powered", powered);
}
