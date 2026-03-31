from collections import deque

class Maze:
    def __init__(self, filename):
        """Load maze from file"""
        with open(filename, 'r') as f:
            contents = f.read().splitlines()
        
        # Validate input
        if not contents:
            raise ValueError("Maze file is empty")
        
        # Determine dimensions
        self.height = len(contents)
        self.width = max(len(line) for line in contents) if contents else 0
        
        # Ensure all rows have same width (pad with spaces if needed)
        self.maze = []
        for i in range(self.height):
            row = contents[i]
            row = row.ljust(self.width)
            self.maze.append(list(row))
        
        # Find start and goal
        self.start = None
        self.goal = None
        
        for i in range(self.height):
            for j in range(self.width):
                if self.maze[i][j] == 'A':
                    self.start = (i, j)
                elif self.maze[i][j] == 'B':
                    self.goal = (i, j)
        
        if self.start is None:
            raise ValueError("Maze has no start point (A)")
        if self.goal is None:
            raise ValueError("Maze has no goal point (B)")
    
    def print(self):
        """Print maze to console"""
        for i in range(self.height):
            for j in range(self.width):
                print(self.maze[i][j], end="")
            print()
        print()
    
    def neighbors(self, state):
        """Return list of valid neighboring cells"""
        row, col = state
        candidates = [
            (row - 1, col),  # Up
            (row + 1, col),  # Down
            (row, col - 1),  # Left
            (row, col + 1)   # Right
        ]
        
        valid_neighbors = []
        for r, c in candidates:
            # Check if within bounds
            if 0 <= r < self.height and 0 <= c < self.width:
                # Check if not a wall
                if self.maze[r][c] != '#':
                    valid_neighbors.append((r, c))
        
        return valid_neighbors
    
    def solve(self):
        """
        Solves maze using BFS.
        Returns list of coordinates representing the path from start to goal.
        """
        start = self.start
        goal = self.goal
        
        # Queue stores tuples of (state, path_to_state)
        queue = deque([(start, [])])
        visited = set([start])
        
        while queue:
            state, path = queue.popleft()
            
            # If goal reached, return solution
            if state == goal:
                return path + [state]
            
            # Explore neighbors
            for neighbor in self.neighbors(state):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [state]))
        
        # No solution found
        return None
    
    def output(self, solution):
        """
        Mark solution path on maze with asterisks.
        Then print the maze.
        """
        if solution is None:
            print("No solution found.")
            return
        
        # Create copy of maze for output
        output_maze = [row[:] for row in self.maze]
        
        # Mark solution path with asterisks (except start and goal)
        for i, (row, col) in enumerate(solution):
            if output_maze[row][col] not in ('A', 'B'):
                output_maze[row][col] = '*'
        
        # Print output maze
        for row in output_maze:
            print(''.join(row))


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")
    
    m = Maze(sys.argv[1])
    print("Maze:")
    m.print()
    
    print("Solving...")
    solution = m.solve()
    
    print("Solution:")
    m.output(solution)
