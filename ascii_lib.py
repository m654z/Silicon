import pprint

class AsciiArt:
    grid = [
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
            ['','','','','','','','','',''],
        ]
    original_grid = grid
    
    def clear(self):
        self.grid = self.original_grid

    def draw(self, x, y, c):
        self.grid[x][y] = c

    def move(self, x, y, x2, y2):
        self.grid[x2][y2] = self.grid[x][y]
        self.grid[x][y] = ''

    def erase(self, x, y):
        self.grid[x][y] = ''

    def draw_ground(self):
        for i in range(0, 9):
            self.grid[9][i] == '_'

    def draw_ceil(self):
        for i in range(0, 9):
            self.grid[0][i] == '-'

    def output(self):
        pprint(''.join(self.grid))
