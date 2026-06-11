class MazeModel:
    def __init__(self, file_path):
        self.grid = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove the trailing newline character
                clean_line = line.rstrip('\r\n')
                # CRITICAL FIX: Replace non-breaking spaces with standard ASCII spaces
                clean_line = clean_line.replace('\xa0', ' ')
                self.grid.append(list(clean_line))

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
        return self.grid[r][c]

    def set_symbol(self, r, c, symbol):
        self.grid[r][c] = symbol