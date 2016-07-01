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
        """Clear the grid."""
        self.grid = self.original_grid

    def draw(self, x, y, c):
        """Draw a character at a certain position."""
        self.grid[x][y] = c

    def move(self, x, y, x2, y2):
        """Move a character from a certain position to another, erasing
        the original character."""
           
        self.grid[x2][y2] = self.grid[x][y]
        self.grid[x][y] = ''

    def erase(self, x, y):
        """Erase a character."""
        self.grid[x][y] = ''

    def draw_box(self, tx, ty, bx, by, k):
        """Draw a box."""
        p = ty
        p2 = tx
        if k == 0:
            self.grid[tx][ty] = '+'
            self.grid[bx][by] = '+'
            while self.grid[tx][p-(by-tx)] != '+':
                self.grid[p2][ty] == '-'
                p += 1

    def output(self):
        """Pretty print the grid."""
        pprint(''.join(self.grid))

a = AsciiArt()
