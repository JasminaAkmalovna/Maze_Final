import unittest
import os
from src.maze_model import MazeModel
from src.solvers.bfs import solve_bfs

class TestBFSSolver(unittest.TestCase):
    def setUp(self):
        self.fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.small_maze_path = os.path.join(self.fixture_dir, 'small.txt')

    def test_bfs_finds_solution_status(self):
        """Step 1: Does the BFS solver return True when a maze has a valid path?"""
        maze = MazeModel(self.small_maze_path)
        
        # Act
        result = solve_bfs(maze)
        
        # Assert
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()