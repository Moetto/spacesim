#include "symbol.h"

Symbol::Symbol(std::shared_ptr<Symbol> u,
               std::shared_ptr<Symbol> l,
               std::shared_ptr<Symbol> r,
               std::shared_ptr<Symbol> d) {
    state = unpowered;
    next_state = unknown;
    is_power_source = false;
}

Symbol::Symbol() {
    state = unpowered;
    next_state = unknown;
    is_power_source = false;
}

void Symbol::reset() {
    next_state = unknown;
    simulated = false;
}

void Symbol::simulate() {
    if (simulated)
        return;
    simulated = true;

    if (is_power_source) {
        next_state = powered;
    }
    else if (next_state == unknown) {
        for (int d = UP; d <= DOWN; d++) {
            auto dir = static_cast<Direction >(d);
            if (getsPowerFrom(dir)) {
                next_state = powered;
                break;
            }
        }
    }

    for (int d = UP; d <= DOWN; d++) {
        auto dir = static_cast<Direction >(d);
        if (hasOutputTo(dir)) {
            get_neighbour(dir)->simulate();
        }
    }
}

void Symbol::switchState() {
    if (next_state == unknown) {
        state = unpowered;
        return;
    }
    state = next_state;
}

std::string Symbol::repr() const {
    return "S " + std::to_string(this->state);
}

std::string Symbol::getChar() {
    return "S";
}

bool Symbol::hasInputFrom(Direction d) {
    if (inputs.count(d) == 0) {
        return false;
    }

    switch (d) {
        case UP:
            if (this->up != nullptr && this->up->outputs.count(DOWN) == 1) {
                return true;
            }
        case LEFT:
            if (this->left != nullptr && this->left->outputs.count(RIGHT) == 1) {
                return true;
            }
        case RIGHT:
            if (this->right != nullptr && this->right->outputs.count(LEFT) == 1) {
                return true;
            }
        case DOWN:
            if (this->down != nullptr && this->down->outputs.count(UP) == 1) {
                return true;
            }
        default:
            return false;
    }
}

bool Symbol::hasOutputTo(Direction d) {
    auto nei = get_neighbour(d);
    if (nei == nullptr) {
        return false;
    }
    d = getOpposite(d);

    return nei->hasInputFrom(d);
}

bool Symbol::getsPowerFrom(Direction d) {
    return (hasInputFrom(d) && this->get_neighbour(d)->isPowered());
}

bool Symbol::isPowered() {
    if (is_power_source) {
        return true;
    }

    for (int d = UP; d <= DOWN; d++) {
        auto dir = static_cast<Direction >(d);
        if (hasInputFrom(dir) && get_neighbour(dir)->next_state == powered)
            return true;
    }
    return false;
}

std::shared_ptr<Symbol> Symbol::get_neighbour(Direction d) {
    switch (d) {
        case UP:
            return this->up;
        case LEFT:
            return this->left;
        case RIGHT:
            return this->right;
        case DOWN:
            return this->down;
        default:
            return nullptr;
    }
}


