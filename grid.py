from components import Empty, get_component


class Grid:
    def __init__(self, width, height):
        self.grid = []
        self.width = width
        self.height = height
        for _y in range(height - 1):
            row = []
            for _x in range(width - 1):
                row.append(Empty.get_empty())
            self.grid.append(row)
        self.link()

    @classmethod
    def load(cls, filename):
        f = open(filename, 'r')
        grid = []
        for line in f:
            row = []
            for char in line.strip("\n"):
                cls_symbol = get_component(char)
                row.append(cls_symbol.get_empty())
            if row:
                grid.append(row)
        g = Grid(len(grid[0]), len(grid))
        g.grid = grid
        g.link()
        f.close()
        return g

    def link(self):
        for _y in range(self.height - 1):
            for _x in range(self.width - 1):
                s = self.grid[_y][_x]
                row = self.grid[_y]

                if _x > 0:
                    left = row[_x - 1]
                else:
                    left = Empty.get_empty()
                left.right = s
                s.left = left

                if _x < self.width - 2:
                    right = row[_x + 1]
                else:
                    right = Empty.get_empty()
                right.left = s
                s.right = right

                if _y > 0:
                    up = self.grid[_y - 1][_x]
                else:
                    up = Empty.get_empty()

                up.down = s
                s.up = up

                if _y < self.height - 2:
                    down = self.grid[_y + 1][_x]
                else:
                    down = Empty.get_empty()
                down.up = s
                s.down = down

    def save(self, filename):
        content = ""
        for line in self.grid:
            row = "".join([symbol.char for symbol in line])
            content += row + "\n"
        file = open(filename, 'w')
        file.write(content)
        file.close()
