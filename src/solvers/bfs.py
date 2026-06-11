from collections import deque

def solve_bfs(maze_model):
    start_pos = maze_model.get_start_position()
    end_pos = maze_model.get_end_position()
    
    # The queue stores tuples of: (current_row, current_col)
    queue = deque([start_pos])
    
    # To keep track of where we came from, we'll use a dictionary:
    # key: (child_row, child_col) -> value: (parent_row, parent_col)
    parent_map = {start_pos: None}
    
    while queue:
        r, c = queue.popleft()
        
        # Base Case: We found the exit!
        if (r, c) == end_pos:
            return True
            
        # Explore neighbors: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # 1. Bounds check
            if nr < 0 or nr >= maze_model.get_height() or nc < 0 or nc >= maze_model.get_width():
                continue
                
            # 2. Wall check and duplicate check
            if maze_model.get_symbol(nr, nc) == '#' or (nr, nc) in parent_map:
                continue
                
            # Document the relationship and add to queue
            parent_map[(nr, nc)] = (r, c)
            queue.append((nr, nc))
            
    return False