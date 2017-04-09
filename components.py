from ports import *
from direction import Direction


class State:
    def __init__(self, power=False):
        self.power = power


class Symbol:
    char = None
    state = State()
    new_state = State()
    up_port = Blocked()
    down_port = Blocked()
    left_port = Blocked()
    right_port = Blocked()
    _power_sources = set()

    def __init__(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __str__(self):
        return self.char

    def __repr__(self):
        return self.char

    def next_symbol(self):
        raise NotImplementedError

    def is_power_source(self):
        return False

    def get_port(self, direction):
        if direction == Direction.UP:
            return self.up_port
        if direction == Direction.DOWN:
            return self.down_port
        if direction == Direction.LEFT:
            return self.left_port
        if direction == Direction.RIGHT:
            return self.right_port

    def _get_neighbouring_symbol(self, direction):
        if direction == Direction.UP:
            return self.up
        if direction == Direction.DOWN:
            return self.down
        if direction == Direction.LEFT:
            return self.left
        if direction == Direction.RIGHT:
            return self.right

    def _is_connected_from(self, direction):
        neighbour = self._get_neighbouring_symbol(direction)
        neighbour_port = neighbour.get_port(Direction.get_opposite_direction(direction))
        if isinstance(self.get_port(direction), Input) and isinstance(neighbour_port, Output):
            return True
        return False

    def is_powered(self):
        for ps in self._power_sources:
            if ps.state.power:
                return True
        return False

    def get_power_sources(self):
        return self._power_sources

    def calculate_new_state(self):
        self.new_state = State()
        for direction in Direction:
            if self._is_connected_from(direction):
                self._power_sources = self._power_sources | self._get_neighbouring_symbol(direction).get_power_sources()
        self.new_state = State(self.is_powered())

    def switch_to_new_state(self):
        self.state = self.new_state
        self.new_state = None

    def reset(self):
        self._power_sources = set()
        self.state = State()
        self.new_state = State()
        if self.is_power_source():
            self._power_sources.add(self)

    @classmethod
    def from_symbol(cls, symbol):
        s = cls(symbol.up, symbol.down, symbol.left, symbol.right)
        s.up.down = s
        s.down.up = s
        s.left.right = s
        s.right.left = s
        return s


class Empty(Symbol):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = ' '

    def next_symbol(self):
        return HorizontalLine.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()

    def is_powered(self):
        return False

    @classmethod
    def get_empty(cls):
        return Empty(None, None, None, None)


class HorizontalLine(Symbol):
    left_port = InputOutput()
    right_port = InputOutput()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '-'

    def next_symbol(self):
        return VerticalLine.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()
        for direction in Direction.LEFT, Direction.RIGHT:
            if self._is_connected_from(direction):
                self._power_sources = self._power_sources | self._get_neighbouring_symbol(direction).get_power_sources()
        self.new_state = State(self.is_powered())


class VerticalLine(Symbol):
    up_port = InputOutput()
    down_port = InputOutput()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '|'

    def next_symbol(self):
        return Cross.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State()
        for direction in Direction.UP, Direction.DOWN:
            if self._is_connected_from(direction):
                self._power_sources = self._power_sources | self._get_neighbouring_symbol(direction).get_power_sources()
        self.new_state = State(self.is_powered())


class Cross(Symbol):
    left_port = InputOutput()
    right_port = InputOutput()
    up_port = InputOutput()
    down_port = InputOutput()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = '+'

    def next_symbol(self):
        return Battery.from_symbol(self)


class Battery(Symbol):
    up_port = Output()
    down_port = Output()
    left_port = Output()
    right_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'B'
        self._power_sources = {self}

    def is_power_source(self):
        return True

    def next_symbol(self):
        return Engine.from_symbol(self)

    def is_powered(self):
        return True

    def calculate_new_state(self):
        self.new_state = State(True)


class Engine(Symbol):
    up_port = Input()
    down_port = Input()
    left_port = Input()
    right_port = Input()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'E'

    def next_symbol(self):
        return PortAnd.from_symbol(self)


class LogicPort(Symbol):
    def is_power_source(self):
        return True

    def get_power_sources(self):
        return {self}


class PortAnd(LogicPort):
    left_port = Input()
    right_port = Input()
    down_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'T'
        self._power_sources = {self}

    def next_symbol(self):
        return PortOr.from_symbol(self)

    def is_powered(self):
        for direction in Direction.LEFT, Direction.RIGHT:
            if not self._is_connected_from(direction) or not self._get_neighbouring_symbol(direction).is_powered():
                return False
        return True

    def calculate_new_state(self):
        self.new_state = State(self.is_powered())


class PortOr(LogicPort):
    left_port = Input()
    right_port = Input()
    down_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'Y'

    def next_symbol(self):
        return PortNot.from_symbol(self)

    def is_powered(self):
        for direction in Direction.LEFT, Direction.RIGHT:
            if self._is_connected_from(direction) and self._get_neighbouring_symbol(direction).is_powered():
                return True
        return False

    def calculate_new_state(self):
        self.new_state = State(self.is_powered())


class PortNot(LogicPort):
    up_port = Input()
    down_port = Output()

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'i'

    def next_symbol(self):
        return Button.from_symbol(self)

    def is_powered(self):
        if self._is_connected_from(Direction.UP) and self._get_neighbouring_symbol(Direction.UP).is_powered():
            return True
        return False

    def calculate_new_state(self):
        self.new_state = State(not self.is_powered())


class Button(Symbol):
    up_port = Output()
    down_port = Output()
    left_port = Output()
    right_port = Output()
    pressed = False

    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        self.char = 'b'
        self._power_sources.add(self)

    def next_symbol(self):
        return Empty.from_symbol(self)

    def calculate_new_state(self):
        self.new_state = State(self.pressed)

    def is_power_source(self):
        return True
