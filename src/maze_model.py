class MazeModel:
    def __init__(self, file_path):
        self.grid = []
        with open(file_path, 'r') as f:
            for line in f:
                self.grid.append(line.strip())

    def get_height(self):
        return len(self.grid)

    def get_width(self):
        return len(self.grid[0]) if self.grid else 0

    def get_start_position(self):
        # Scan every row and column for 'S'
        for r in range(self.get_height()):
            for c in range(self.get_width()):
                if self.grid[r][c] == 'S':
                    return (r, c)
        return None

    def get_end_position(self):
        # Scan every row and column for 'E'
        for r in range(self.get_height()):
            for c in range(self.get_width()):
                if self.grid[r][c] == 'E':
                    return (r, c)
        return None