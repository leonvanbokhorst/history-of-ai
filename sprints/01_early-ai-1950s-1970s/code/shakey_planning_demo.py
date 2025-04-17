# shakey_planning_demo.py
# Stub for a simple grid-world planner

def plan(start, goal, grid):
    """
    Plan a path from start to goal in a grid
    """
    # BFS
    queue = [start]
    visited = set()
    while queue:
        current = queue.pop(0)
        if current == goal:
            return current
        visited.add(current)
        queue.extend(
            neighbor
            for neighbor in get_neighbors(current, grid)
            if neighbor not in visited
        )
    return None

def get_neighbors(state, grid):
    """
    Get the neighbors of a state in a grid
    """
    x, y = state
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < len(grid)-1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < len(grid[0])-1:
        neighbors.append((x, y+1))
    return neighbors

def get_path(node):
    """
    Get the path from the start to the goal
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def main():
    """
    Main function to run the planning demo
    """
    grid = [
        [0, 0, 0, 0],       
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (2, 3)
    path = plan(start, goal, grid)
    print(path)

if __name__ == "__main__":
    main()

