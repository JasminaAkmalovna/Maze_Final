import heapq

def manhattan_distance(p1, p2):
    """Calculate the Manhattan distance between two coordinates."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve_astar(maze_model):
    start_pos = maze_model.get_start_position()
    end_pos = maze_model.get_end_position()
    
    # Priority queue stores tuples of: (f_score, current_pos)
    # heapq in Python always sorts by the first element of the tuple
    open_set = []
    heapq.heappush(open_set, (0, start_pos))
    
    # Track the lowest cost to reach each node from the start position
    g_score = {start_pos: 0}
    
    # Track parent relationships for backtracking the path later
    parent_map = {start_pos: None}
    
    # Track which nodes have been completely processed
    closed_set = set()
    
    while open_set:
        # Get the node with the lowest f_score
        _, current = heapq.heappop(open_set)
        
        # Base Case: Target found!
        if current == end_pos:
            # Backtrack to draw the optimal path with '+'
            curr = parent_map[end_pos]
            while curr and curr != start_pos:
                maze_model.set_symbol(curr[0], curr[1], '+')
                curr = parent_map[curr]
            return True
            
        closed_set.add(current)
        r, c = current
        
        # Explore neighbors: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            
            # 1. Bounds check
            if nr < 0 or nr >= maze_model.get_height() or nc < 0 or nc >= maze_model.get_width():
                continue
                
            # 2. Wall check or already completely processed check
            if maze_model.get_symbol(nr, nc) == '#' or neighbor in closed_set:
                continue
                
            # Tentative g_score: steps from start to current + 1 step to neighbor
            tentative_g = g_score[current] + 1
            
            # If we found a shorter path to this neighbor, or haven't seen it yet
            if tentative_g < g_score.get(neighbor, float('inf')):
                parent_map[neighbor] = current
                g_score[neighbor] = tentative_g
                
                # f_score = g_score (exact cost) + h_score (estimated cost to exit)
                f_score = tentative_g + manhattan_distance(neighbor, end_pos)
                
                # Visually mark it as an explored cell if it's not the exit
                if neighbor != end_pos:
                    maze_model.set_symbol(nr, nc, '^')
                    
                heapq.heappush(open_set, (f_score, neighbor))
                
    return False