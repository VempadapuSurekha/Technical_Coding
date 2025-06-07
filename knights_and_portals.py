"""
Problem 3: Knights and Portals

Given a grid, find the shortest path from top-left to bottom-right. You may teleport between any two empty cells exactly once.
"""

from collections import deque

def shortest_path_with_portal(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    def bfs(used_portal):
        visited = set()
        queue = deque([(0, 0, 0, used_portal)])
        empty = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

        while queue:
            r, c, steps, used = queue.popleft()
            if (r, c) == (rows-1, cols-1):
                return steps
            visited.add((r, c, used))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc, used) not in visited:
                    queue.append((nr, nc, steps + 1, used))

            if not used:
                for pr, pc in empty:
                    if (pr, pc) != (r, c) and (pr, pc, True) not in visited:
                        queue.append((pr, pc, steps + 1, True))
    return bfs(False)


if __name__ == "__main__":
    grid = [
      [0, 1, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print("Expected: 4")
    print("Output:", shortest_path_with_portal(grid))
