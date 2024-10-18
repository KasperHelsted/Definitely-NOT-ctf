import copy


# Check if placing a value in the cell is valid according to Sudoku rules
def is_valid(board, row, col, num):
    # Check if num is in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check if num is in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if num is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


# Backtracking function to solve the Sudoku and collect all solutions
def solve_sudoku_all(board, possibles, solutions):
    empty_cell = find_empty(board)
    if not empty_cell:
        solutions.append(copy.deepcopy(board))  # Add the current valid solution
        return

    row, col = empty_cell

    # Try each possible value for the current cell
    for num in possibles[row][col]:
        if is_valid(board, row, col, num):
            board[row][col] = num
            solve_sudoku_all(board, possibles, solutions)
            board[row][col] = 0  # Reset on backtrack


# Function to find an empty cell in the board (cells with a value of 0)
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# Function to print the board (for display purposes)
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


# Example input
# An empty Sudoku board (0 represents an empty cell)
board = [[0] * 9 for _ in range(9)]

# Possible values in each cell (Example: you need to populate this with your possibilities)
possibles = [
    [[5], [3], [1, 2, 4], [2, 4, 6], [7], [4, 6], [1, 4, 6], [1, 4, 6], [1, 2, 4]],
    [[6], [1, 2, 4], [1, 2, 3, 4, 7], [1], [9], [5], [3, 4, 7], [1, 3, 4, 7], [1, 2, 4, 7]],
    [[1, 2, 3, 4], [9], [8], [2, 3], [3, 4], [2, 4], [1, 3, 4, 5, 7], [6], [1, 2, 4, 5]],
    [[8], [1, 2, 5], [1, 2, 5, 7], [2, 5, 7, 9], [6], [2, 4, 5, 7], [1, 2, 4, 5, 7, 9], [1, 2, 4, 5, 9], [3]],
    [[4], [1, 2, 5], [1, 2, 5, 7], [8], [2, 5], [3], [1, 2, 5, 7, 9], [1, 2, 5, 9], [1]],
    [[7], [1, 2, 3, 4, 9], [1, 2, 3, 4, 5, 9], [2, 5, 9], [2], [2, 4], [1, 2, 4, 5, 9], [1, 2, 4, 9], [6]],
    [[1, 2, 3, 4, 9], [6], [1, 2, 3, 4, 5, 7, 9], [2, 5, 9], [3, 4, 5, 7, 9], [1, 4, 5], [2], [8], [1, 2, 4, 5]],
    [[1, 2, 3, 9], [1, 2, 3, 8], [1, 2, 3, 8], [4], [1], [9], [1, 3, 4, 6], [1, 3, 4, 6], [5]],
    [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 6], [1, 3, 5], [8], [1, 3, 4, 6], [1, 3, 4], [7], [9]]
]

# List to hold all solutions
solutions = []

# Solve the puzzle and collect all solutions
solve_sudoku_all(board, possibles, solutions)

# Print all solutions
print(f"Number of solutions found: {len(solutions)}")
for index, solution in enumerate(solutions, 1):
    print(f"\nSolution {index}:")
    print_board(solution)
