"""
Problem 5: Matrix Islands with Diagonals

Count the number of islands in a matrix of 0s and 1s.
Islands are formed using horizontal, vertical, or diagonal connections.
"""

def count_islands(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or matrix[r][c] == 0:
            return
        visited[r][c] = True
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                count += 1
    return count


if __name__ == "__main__":
    matrix = [
        [1, 1, 0],
        [0, 1, 0],
        [1, 0, 1]
    ]
    print("Expected: 2")
    print("Output:", count_islands(matrix))
