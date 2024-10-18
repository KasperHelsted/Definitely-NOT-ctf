# Import sys to set recursion limit
import sys
sys.setrecursionlimit(100000)

def read_grid(input_str):
    grid = []
    for line in input_str.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('-'):
            continue
        # Remove '|' and split
        tokens = line.replace('|', '').split()
        row = [int(tok) for tok in tokens]
        grid.append(row)
    return grid

def print_grid(grid):
    for i in range(len(grid)):
        if i % 9 == 0 and i != 0:
            print("-" * 75)
        for j in range(len(grid[0])):
            if j % 9 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else '.', end=' ')
        print()

def is_valid(grid, num, row, col):
    # Determine the subgrid
    subgrid_row = (row // 9) * 9
    subgrid_col = (col // 9) * 9

    # Local positions within the subgrid
    local_row = row % 9
    local_col = col % 9

    # Check row within subgrid
    for j in range(subgrid_col, subgrid_col + 9):
        if grid[row][j] == num and j != col:
            return False

    # Check column within subgrid
    for i in range(subgrid_row, subgrid_row + 9):
        if grid[i][col] == num and i != row:
            return False

    # Check 3x3 block within subgrid
    block_row = subgrid_row + (local_row // 3) * 3
    block_col = subgrid_col + (local_col // 3) * 3
    for i in range(block_row, block_row + 3):
        for j in range(block_col, block_col + 3):
            if grid[i][j] == num and (i, j) != (row, col):
                return False

    # Check the central grid constraints if cell is in central grid
    if 3 <= local_row <= 5 and 3 <= local_col <= 5:
        # Map to central grid
        central_row = (row // 9) * 3 + (local_row - 3)
        central_col = (col // 9) * 3 + (local_col - 3)
        # Check row in central grid
        for c in range(9):
            if c != central_col and get_central_cell(grid, central_row, c) == num:
                return False
        # Check column in central grid
        for r in range(9):
            if r != central_row and get_central_cell(grid, r, central_col) == num:
                return False
        # Check 3x3 block in central grid
        block_cr = (central_row // 3) * 3
        block_cc = (central_col // 3) * 3
        for i in range(block_cr, block_cr + 3):
            for j in range(block_cc, block_cc + 3):
                if (i, j) != (central_row, central_col) and get_central_cell(grid, i, j) == num:
                    return False

    return True

def get_central_cell(grid, central_row, central_col):
    # Map central grid coordinates back to the main grid
    sgr = central_row // 3
    sgc = central_col // 3
    local_row = (central_row % 3) + 3
    local_col = (central_col % 3) + 3
    row = sgr * 9 + local_row
    col = sgc * 9 + local_col
    # Check if indices are within bounds
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return 0  # Return 0 if out of bounds (should not happen with correct indices)

def set_central_cell(grid, central_row, central_col, value):
    sgr = central_row // 3
    sgc = central_col // 3
    local_row = (central_row % 3) + 3
    local_col = (central_col % 3) + 3
    row = sgr * 9 + local_row
    col = sgc * 9 + local_col
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = value

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None

def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True  # Solved
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, num, row, col):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Backtrack
    return False

# Input Sudoku grid as provided
input_grid = """
 ------------------------------------------------------------
| 0 3 0 0 7 0 6 0 2 | 8 0 0 2 0 6 0 0 3 | 9 0 2 0 3 0 0 8 0 | 
| 6 9 0 0 1 0 5 0 0 | 9 0 0 0 0 0 0 0 2 | 0 0 7 0 1 0 0 6 2 | 
| 0 0 0 5 0 6 3 0 0 | 3 0 0 8 0 5 0 0 7 | 0 0 8 5 0 2 0 0 0 | 
| 0 0 1 0 0 0 0 5 0 | 0 0 3 0 0 0 5 0 0 | 0 1 0 0 0 0 8 0 0 | 
| 8 6 0 0 0 0 0 0 1 | 0 9 0 0 0 0 0 3 0 | 7 0 0 0 0 0 0 2 9 | 
| 0 0 2 0 0 0 0 3 8 | 0 1 0 0 0 0 0 9 0 | 3 2 0 0 0 0 6 0 0 | 
| 5 1 7 0 0 0 0 0 0 | 7 0 0 6 0 1 0 0 8 | 0 0 0 0 0 0 2 3 8 | 
| 0 0 0 2 0 9 0 0 0 | 0 8 0 0 0 0 0 7 0 | 0 0 0 9 0 3 0 0 0 | 
| 2 0 0 0 5 1 0 0 0 | 1 0 4 0 7 0 6 0 9 | 0 0 0 1 4 0 0 0 6 | 
 ------------------------------------------------------------
| 6 1 2 0 0 0 7 0 4 | 0 9 0 6 0 5 0 3 0 | 4 0 3 0 0 0 7 9 8 | 
| 0 0 0 0 8 1 0 5 0 | 5 0 4 0 0 0 1 0 9 | 0 9 0 5 4 0 0 0 0 | 
| 0 0 0 4 0 0 0 0 3 | 0 6 0 1 0 2 0 4 0 | 1 0 0 0 0 7 0 0 0 | 
| 5 0 6 0 0 0 8 0 0 | 9 0 2 0 0 0 6 0 4 | 0 0 9 0 0 0 2 0 1 | 
| 0 0 0 0 0 0 0 0 9 | 0 0 0 0 0 0 0 0 0 | 5 0 0 0 0 0 0 0 0 | 
| 2 0 9 0 0 0 6 0 0 | 7 0 5 0 0 0 8 0 2 | 0 0 6 0 0 0 8 0 4 | 
| 0 0 0 1 0 0 0 0 8 | 0 7 0 3 0 4 0 1 0 | 9 0 0 0 0 3 0 0 0 | 
| 0 0 0 0 7 5 0 1 0 | 8 0 1 0 0 0 4 0 3 | 0 6 0 4 5 0 0 0 0 | 
| 1 2 5 0 0 0 3 0 7 | 0 4 0 2 0 1 0 8 0 | 7 0 5 0 0 0 9 4 2 | 
 ------------------------------------------------------------
| 9 0 0 0 3 6 0 0 0 | 4 0 1 0 3 0 7 0 9 | 0 0 0 9 2 0 0 0 1 | 
| 0 0 0 4 0 9 0 0 0 | 0 9 0 0 0 0 0 2 0 | 0 0 0 7 0 4 0 0 0 | 
| 2 4 6 0 0 0 0 0 0 | 7 0 0 1 0 9 0 0 4 | 0 0 0 0 0 0 4 9 5 | 
| 0 0 7 0 0 0 0 8 5 | 0 8 0 0 0 0 0 5 0 | 1 6 0 0 0 0 3 0 0 | 
| 1 9 0 0 0 0 0 0 3 | 0 7 0 0 0 0 0 8 0 | 7 0 0 0 0 0 0 8 4 | 
| 0 0 2 0 0 0 0 1 0 | 0 0 5 0 0 0 6 0 0 | 0 8 0 0 0 0 1 0 0 | 
| 0 0 0 1 0 7 3 0 0 | 5 0 0 9 0 4 0 0 8 | 0 0 8 2 0 9 0 0 0 | 
| 3 1 0 0 4 0 7 0 0 | 9 0 0 0 0 0 0 0 6 | 0 0 5 0 8 0 0 1 7 | 
| 0 7 0 0 8 0 1 0 4 | 8 0 0 7 0 6 0 0 3 | 9 0 6 0 5 0 0 4 0 | 
 ------------------------------------------------------------
"""

grid = read_grid(input_grid)

print("Original Sudoku grid:")
print_grid(grid)

if solve_sudoku(grid):
    print("\nSolved Sudoku grid:")
    print_grid(grid)
else:
    print("No solution exists.")
