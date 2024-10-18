from glob import glob


def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            row += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print("- " * 11)

def find_empty(board):
    """Finds an empty cell in the Sudoku board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    """Checks whether it's valid to place num at the given position."""
    row, col = pos

    # Check row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 block
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Reset the cell and backtrack

    return False  # Trigger backtracking


for file in glob('./boards/*.txt'):
    with open(file, 'r') as f:
        data = []
        for line in f.readlines():
            data.append([int(x) for x in line.split()])

    print("Original Sudoku Puzzle:")
    print_board(data)

    if solve(data):
        print("\nSolved Sudoku Puzzle:")
        print_board(data)
    else:
        print("No solution exists for the given Sudoku puzzle.")
    exit()