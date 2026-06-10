import unittest
import os
from src.maze_model import MazeModel

class TestMazeModel(unittest.TestCase):
    def setUp(self):
        # Find the absolute path to our test file
        self.fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.small_maze_path = os.path.join(self.fixture_dir, 'small.txt')

    def test_maze_loading(self):
        """Step 1: Can we load a file and accurately parse its rows and columns?"""
        maze = MazeModel(self.small_maze_path)
        
        # small.txt has 5 rows and 6 columns
        self.assertEqual(maze.get_height(), 5)
        self.assertEqual(maze.get_width(), 6)

    def test_find_start_and_end(self):
        """Step 2: Can our model identify where 'S' and 'E' are located?"""
        maze = MazeModel(self.small_maze_path)
        
        # In small.txt, 'S' is at row 1, column 1. 'E' is at row 3, column 4.
        self.assertEqual(maze.get_start_position(), (1, 1))
        self.assertEqual(maze.get_end_position(), (3, 4))

if __name__ == '__main__':
    unittest.main()