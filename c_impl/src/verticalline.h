//
// Created by t3mu on 23/06/18.
//

#ifndef SIMULINK_VERTICALLINE_H
#define SIMULINK_VERTICALLINE_H

#include "line.h"

class VerticalLine : public Line {
public:
    VerticalLine();

    VerticalLine(std::shared_ptr<Symbol> u,
                 std::shared_ptr<Symbol> l,
                 std::shared_ptr<Symbol> r,
                 std::shared_ptr<Symbol> d);

    std::string repr() const override;

    std::string getChar() override;
};

#endif //SIMULINK_VERTICALLINE_H
