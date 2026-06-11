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
        
        # --- ADD THESE LINES TO PRINT DEBUG ---
        print("\n--- DEBUG MAZE ---")
        for row in maze.grid:
            print("".join(row))
        print(f"Start pos: {maze.get_start_position()}")
        print(f"End pos: {maze.get_end_position()}")
        print("------------------")
        
        result = solve_dfs(maze)
        self.assertTrue(result)

    def test_dfs_marks_visited_nodes(self):
        """Step 2: Does the solver mark visited nodes correctly?"""
        maze = MazeModel(self.small_maze_path)
        
        solve_dfs(maze)
        
        # (2, 1) is part of the final correct path, so it must be '+'
        self.assertEqual(maze.get_symbol(2, 1), '+')

if __name__ == '__main__':
    unittest.main()