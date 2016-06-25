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

    def draw_ground(self):
        """Draw multiple _s at the bottom of the grid."""
        for i in range(0, 9):
            self.grid[9][i] == '_'

    def draw_ceil(self):
        """Draw multiple -s at the top of the grid."""
        for i in range(0, 9):
            self.grid[0][i] == '-'

    def output(self):
        """Pretty print the grid."""
        pprint(''.join(self.grid))
