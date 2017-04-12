#include <boost/python.hpp>
//#include <iostream>
#include "grid.h"
#include "symbol.h"


BOOST_PYTHON_MODULE(simulink)
{
    using namespace boost::python;
    class_<Symbol>("Symbol")
        .def("__repr__", &Symbol::repr);
    class_<Grid>("Grid", init<int, int>())
        .def("get_item", &Grid::get_item);
}
