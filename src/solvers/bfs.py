from collections import deque

def solve_bfs(maze_model):
    start_pos = maze_model.get_start_position()
    end_pos = maze_model.get_end_position()
    
    queue = deque([start_pos])
    parent_map = {start_pos: None}
    
    while queue:
        r, c = queue.popleft()
        
        # Base Case: We found the exit! 
        if (r, c) == end_pos:
            # --- BACKTRACKING TO DRAW THE FINAL SHORTEST PATH ---
            # Start from the cell right before the exit
            curr = parent_map[end_pos]
            while curr and curr != start_pos:
                maze_model.set_symbol(curr[0], curr[1], '+')
                curr = parent_map[curr]
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
                
            # Document parent-child relationship
            parent_map[(nr, nc)] = (r, c)
            
            # If it's not the end goal, visually mark it as an explored/visited cell
            if (nr, nc) != end_pos:
                maze_model.set_symbol(nr, nc, '^')
                
            queue.append((nr, nc))
            
    return False