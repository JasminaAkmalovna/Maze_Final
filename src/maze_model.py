class MazeModel:
    def __init__(self, file_path):
        self.grid = []
        # Read the file and strip newline characters
        with open(file_path, 'r') as f:
            for line in f:
                self.grid.append(line.strip())

    def get_height(self):
        return len(self.grid)

    def get_width(self):
        # If the grid has rows, return the length of the first row
        return len(self.grid[0]) if self.grid else 0

    def get_start_position(self):
        # Leaving this wrong on purpose for our next baby step
        return (0, 0)

    def get_end_position(self):
        # Leaving this wrong on purpose for our next baby step
        return (0, 0)