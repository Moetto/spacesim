//
// Created by t3mu on 23/06/18.
//

#ifndef SIMULINK_VERTICALLINE_H
#define SIMULINK_VERTICALLINE_H

#include "line.h"

class VerticalLine : public Line {
public:
    using Line::Line;

    std::string repr() const override;

    std::string getChar() override;
};

#endif //SIMULINK_VERTICALLINE_H
