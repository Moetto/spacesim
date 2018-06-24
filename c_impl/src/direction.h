//
// Created by t3mu on 23/06/18.
//

#ifndef SIMULINK_DIRECTION_H
#define SIMULINK_DIRECTION_H
enum Direction {
    UP = 0, LEFT=1, RIGHT=2, DOWN=3
};

Direction getOpposite(Direction d );

#endif //SIMULINK_DIRECTION_H
