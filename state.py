class State:
    def __init__(self, message, draw_power, cursor_x, cursor_y, grid_x, grid_y):
        self.message = message
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.show_power = draw_power
