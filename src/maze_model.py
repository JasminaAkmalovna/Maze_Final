class MazeModel:
    def __init__(self, file_path):
        self.grid = []
        with open(file_path, 'r') as f:
            for line in f:
                # Convert string line into a list of characters ['#', 'S', '#', ...]
                self.grid.append(list(line.strip()))

    def get_height(self):
        return len(self.grid)

    def get_width(self):
        return len(self.grid[0]) if self.grid else 0

    def get_start_position(self):
        for r in range(self.get_height()):
            for c in range(self.get_width()):
                if self.grid[r][c] == 'S':
                    return (r, c)
        return None

    def get_end_position(self):
        for r in range(self.get_height()):
            for c in range(self.get_width()):
                if self.grid[r][c] == 'E':
                    return (r, c)
        return None

    def get_symbol(self, r, c):
        """Get character at row r, column c."""
        return self.grid[r][c]

    def set_symbol(self, r, c, symbol):
        """Change character at row r, column c."""
        self.grid[r][c] = symbol