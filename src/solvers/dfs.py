def solve_dfs(maze_model):
    start_pos = maze_model.get_start_position()
    end_pos = maze_model.get_end_position()
    visited = set()

    def explore(r, c):
        if r < 0 or r >= maze_model.get_height() or c < 0 or c >= maze_model.get_width():
            return False
            
        if maze_model.get_symbol(r, c) == '#' or (r, c) in visited:
            return False

        if (r, c) == end_pos:
            return True

        visited.add((r, c))
        if (r, c) != start_pos:  
            maze_model.set_symbol(r, c, '^')

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            if explore(r + dr, c + dc):
                if (r, c) != start_pos:
                    maze_model.set_symbol(r, c, '+')
                return True

        return False

    return explore(start_pos[0], start_pos[1])