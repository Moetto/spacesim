#include "direction.h"
Direction getOpposite(Direction d){
switch (d) {
case UP:
return DOWN;
case DOWN:
return UP;
case LEFT:
return RIGHT;
case RIGHT:
return LEFT;
}
}

