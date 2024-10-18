# import json
#
# with open('centroids.json', 'r') as f:
#     data = json.load(f)
#
# board = [[], [], [], [], [], [], [], [], []]
#
#
# def is_valid_sudoku(board):
#     def is_valid_unit(unit):
#         return len(unit) == len(set(unit))  # Check for duplicates
#
#     # Check rows
#     for row in board:
#         if not is_valid_unit(row):
#             return False
#
#     # Check columns
#     for col in zip(*board):
#         if not is_valid_unit(col):
#             return False
#
#     # Check 3x3 sub-grids
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#             if not is_valid_unit(subgrid):
#                 return False
#
#     return True
#
#
# for k1, v1 in data['board1'].items():
#     for k2, v2 in data['board2'].items():
#         for k3, v3 in data['board3'].items():
#             test1 = [v1[0] + v2[0] + v3[0], v1[1] + v2[1] + v3[1], v1[2] + v2[2] + v3[2]]
#
#             for k4, v4 in data['board4'].items():
#                 for k5, v5 in data['board5'].items():
#                     for k6, v6 in data['board6'].items():
#                         test2 = [v4[0] + v5[0] + v6[0], v4[1] + v5[1] + v6[1], v4[2] + v5[2] + v6[2]]
#
#                         for k7, v7 in data['board7'].items():
#                             for k8, v8 in data['board8'].items():
#                                 for k9, v9 in data['board9'].items():
#                                     test3 = [v7[0] + v8[0] + v9[0], v7[1] + v8[1] + v9[1], v7[2] + v8[2] + v9[2]]
#                                     if is_valid_sudoku(test1 + test2 + test3):
#                                         print("test")
#                                         exit(1)

import json
from multiprocessing import Pool, Manager

def is_valid_sudoku(board):
    def is_valid_unit(unit):
        return len(unit) == len(set(unit))  # Check for duplicates

    # Check rows
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*board):
        if not is_valid_unit(col):
            return False

    # Check 3x3 sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(subgrid):
                return False

    return True

def process_combinations(args):
    k1_v1, data = args
    k1, v1 = k1_v1
    for k2, v2 in data['board2'].items():
        for k3, v3 in data['board3'].items():
            test1 = [v1[0] + v2[0] + v3[0], v1[1] + v2[1] + v3[1], v1[2] + v2[2] + v3[2]]
            for k4, v4 in data['board4'].items():
                for k5, v5 in data['board5'].items():
                    for k6, v6 in data['board6'].items():
                        test2 = [v4[0] + v5[0] + v6[0], v4[1] + v5[1] + v6[1], v4[2] + v5[2] + v6[2]]
                        for k7, v7 in data['board7'].items():
                            for k8, v8 in data['board8'].items():
                                for k9, v9 in data['board9'].items():
                                    test3 = [v7[0] + v8[0] + v9[0], v7[1] + v8[1] + v9[1], v7[2] + v8[2] + v9[2]]
                                    if is_valid_sudoku(test1 + test2 + test3):
                                        return True  # Found a valid sudoku
    return False  # No valid sudoku found in this branch

def main():
    with open('centroids.json', 'r') as f:
        data = json.load(f)

    with Pool() as pool:
        # Prepare arguments for multiprocessing
        args = [((k1, v1), data) for k1, v1 in data['board1'].items()]
        for result in pool.imap_unordered(process_combinations, args):
            if result:
                print("Valid Sudoku found!")
                pool.terminate()
                break
        else:
            print("No valid Sudoku found.")

if __name__ == '__main__':
    main()