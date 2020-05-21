from sudoku_reader import read_boards
from dlx import dlx_search

with open('../p096_sudoku.txt') as f:
    boards = read_boards(f)

def make_row(value, i, j):
    row = [0] * 324
    row[i * 9 + j] = 1 # row column
    row[81 + i * 9 + value] = 1 # row value
    row[162 + j * 9 + value] = 1 # column value
    box = (i // 3) * 3 + j // 3
    row[243 + box * 9 + value] = 1 # box value
    return row

def sudoku_to_exact_cover(board):
    matrix = [None] * 729
    for i in range(9):
        for j in range(9):
            for v in range(9):
                rown = i * 81 + j * 9 + v
                matrix[rown] = make_row(v, i, j) if not board[i][j] or board[i][j] - 1 == v else [0] * 324
    return matrix

def exact_cover_rows_to_solution(rows):
    board = [[0] * 9 for _ in range(9)]
    for row in rows:
        i = row // 81
        j = (row - i * 81) // 9
        v = row - i * 81 - j * 9
        board[i][j] = v + 1
    return board

def solve_dlx(board):
    return exact_cover_rows_to_solution(next(dlx_search(sudoku_to_exact_cover(board))))

def p96():
    s = 0
    for board in boards:
        print(board)
        solved = solve_dlx(board)
        print(solved)
        s += solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]
    return s
