import unittest
import os
from src.maze_model import MazeModel
from src.solvers.astar import solve_astar

class TestAStarSolver(unittest.TestCase):
    def setUp(self):
        self.fixture_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.small_maze_path = os.path.join(self.fixture_dir, 'small.txt')

    def test_astar_finds_solution_status(self):
        """Step 1: Does the A* solver return True when a maze has a valid path?"""
        maze = MazeModel(self.small_maze_path)
        
        # Act
        result = solve_astar(maze)
        
        # Assert
        self.assertTrue(result)

    def test_astar_marks_visited_and_path(self):
        """Step 2: Does A* correctly mark visited spaces with '^' and the final path with '+'?"""
        maze = MazeModel(self.small_maze_path)
        
        solve_astar(maze)
        
        # (3, 1) is a critical bottleneck tile on the winning path
        self.assertEqual(maze.get_symbol(3, 1), '+')
        
        # (1, 4) is a dead end in the wrong direction. 
        # A*'s heuristic will smartly ignore it, leaving it empty.
        self.assertEqual(maze.get_symbol(1, 4), ' ')

if __name__ == '__main__':
    unittest.main()