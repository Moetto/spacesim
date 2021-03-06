cmake_minimum_required(VERSION 3.10)

project(simulink CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(Python_ADDITIONAL_VERSIONS 3.6)
set(PYTHON_LIBRARY /usr/lib/x86_64-linux-gnu/libpython3.6m.so)
find_package(PythonInterp REQUIRED)
find_package(PythonLibs 3.6 REQUIRED)
find_package(Boost COMPONENTS python REQUIRED)
message("Using python " ${PYTHONLIBS_VERSION_STRING} " with executable " ${PYTHON_EXECUTABLE})
message("Using boost " ${Boost_VERSION})
set(SOURCES
        src/battery.cpp
        src/boost.cpp
        src/crossline.cpp
        src/direction.cpp
        src/empty.cpp src/grid.cpp
        src/horizontalline.cpp
        src/line.cpp
        src/notport.cpp
        src/simulationengine.cpp
        src/symbol.cpp
        src/verticalline.cpp)
include_directories(src ${PYTHON_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS} src)
PYTHON_ADD_MODULE(simulink ${SOURCES})
target_link_libraries(simulink /usr/lib/x86_64-linux-gnu/libboost_python-py36.so ${PYTHON_LIBRARIES}) #${Boost_LIBRARIES})
