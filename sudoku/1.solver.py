import hashlib
import json
import os
from glob import glob
from os.path import basename


# Function to print the Sudoku board
def print_board(board_name, board):
    os.makedirs(f'./solution/{board_name}/', exist_ok=True)

    filename = hashlib.md5(json.dumps(board).encode('utf-8')).hexdigest()

    with open(f'./solution/{board_name}/{filename}.json', 'w') as f:
        json.dump(board, f)


# Function to check if placing a number is valid
def is_valid(board, row, col, num):
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# Function to find an empty cell in the Sudoku grid
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


# Function to solve the Sudoku and print all solutions
def solve_sudoku(board_name, board):
    empty_pos = find_empty(board)
    if not empty_pos:
        print_board(board_name, board)
        return True

    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recursively solve the rest of the board
            if solve_sudoku(board_name, board):
                board[row][col] = 0  # Reset for next solution

    board[row][col] = 0  # Reset the cell
    return False


if __name__ == '__main__':
    for file in glob('./boards/*.txt'):
        board_name, _ = basename(file).split('.')

        with open(file, 'r') as f:
            data = []
            for line in f.readlines():
                data.append([int(x) for x in line.split()])

        solve_sudoku(board_name, data)
