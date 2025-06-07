"""
Problem 1: Sudoku Validator With Custom Zones

Validate a 9x9 Sudoku board. In addition to standard rules (rows, columns, 3x3 grids),
validate additional custom zones (each with 9 unique cells) that must also contain digits 1–9 without repetition.
"""

def is_valid_sudoku(board, custom_zones):
    def is_valid_group(group):
        nums = [cell for cell in group if cell != "."]
        return len(nums) == len(set(nums)) and all(1 <= int(cell) <= 9 for cell in nums)

    for i in range(9):
        row = board[i]
        col = [board[j][i] for j in range(9)]
        if not is_valid_group(row) or not is_valid_group(col):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[r][c] for r in range(box_row, box_row+3) for c in range(box_col, box_col+3)]
            if not is_valid_group(box):
                return False

    for zone in custom_zones:
        zone_cells = [board[i][j] for i, j in zone]
        if not is_valid_group(zone_cells):
            return False

    return True


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    custom_zones = [
        [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)],
        [(0,8),(1,7),(2,6),(3,5),(4,4),(5,3),(6,2),(7,1),(8,0)]
    ]

    print("Expected: True")
    print("Output:", is_valid_sudoku(board, custom_zones))
