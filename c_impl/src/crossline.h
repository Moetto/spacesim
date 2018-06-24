//
// Created by t3mu on 23/06/18.
//

#ifndef SIMULINK_CROSSLINE_H
#define SIMULINK_CROSSLINE_H

#include "line.h"

class CrossLine : public Line{
public:
    CrossLine();

    CrossLine(std::shared_ptr<Symbol> u,
                 std::shared_ptr<Symbol> l,
                 std::shared_ptr<Symbol> r,
                 std::shared_ptr<Symbol> d);

    std::string repr() const override;

    std::string getChar() override;
};


#endif //SIMULINK_CROSSLINE_H
