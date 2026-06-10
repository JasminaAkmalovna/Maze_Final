import unittest
import os
from src.maze_model import MazeModel
from src.solvers.dfs import solve_dfs

class TestDFSSolver(unittest.TestCase):
    def setUp(self):
        self.fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.small_maze_path = os.path.join(self.fixture_dir, 'small.txt')

    def test_dfs_finds_solution_status(self):
        """Step 1: Does the solver return True when a maze has a valid path?"""
        maze = MazeModel(self.small_maze_path)
        
        # Act: Run the solver
        result = solve_dfs(maze)
        
        # Assert: It should successfully return True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()