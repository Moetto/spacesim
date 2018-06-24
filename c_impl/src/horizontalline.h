//
// Created by t3mu on 24/06/18.
//

#ifndef SIMULINK_HORIZONTALLINE_H
#define SIMULINK_HORIZONTALLINE_H
#include "line.h"

class HorizontalLine : public Line{
public:
    HorizontalLine();

    HorizontalLine(std::shared_ptr<Symbol> u,
                 std::shared_ptr<Symbol> l,
                 std::shared_ptr<Symbol> r,
                 std::shared_ptr<Symbol> d);

    std::string repr() const override;

    std::string getChar() override;
};


#endif //SIMULINK_HORIZONTALLINE_H
