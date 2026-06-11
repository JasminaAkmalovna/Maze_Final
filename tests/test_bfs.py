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

    def test_bfs_marks_visited_and_path(self):
        """Step 2: Does BFS correctly mark visited spaces with '^' and the final path with '+'?"""
        maze = MazeModel(self.small_maze_path)
        
        solve_bfs(maze)
        
        # (2, 1) is right under the start position 'S' and is part of the winning path
        self.assertEqual(maze.get_symbol(2, 1), '+')
        
        # (2, 3) is a side corridor that BFS explores, but isn't on the shortest path.
        # It should be marked with '^'.
        self.assertEqual(maze.get_symbol(2, 3), '^')

if __name__ == '__main__':
    unittest.main()