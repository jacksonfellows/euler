from copy import deepcopy

def read_boards(f):
    boards = []
    for i,line in enumerate(f):
        if i % 10 == 0:
            boards.append([])
        else:
            boards[-1].append([int(d) for d in line.strip()])
    return boards

with open('../p096_sudoku.txt') as f:
    boards = read_boards(f)

digits = set(range(1,10))

def row(board, i):
    return board[i]

def col(board, j):
    return [row[j] for row in board]

def cell(board, i, j):
    return [board[(i // 3) * 3 + _i][(j // 3) * 3 + _j] for _i in range(3) for _j in range(3)]

def possibilities(board, i, j):
    return digits - (set(cell(board, i, j)) | set(row(board, i)) | set(col(board, j)))

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                ps = possibilities(board, i, j)
                if len(ps) == 1:
                    board[i][j] = next(iter(ps))
                    continue
                for p in ps:
                    copied_board = deepcopy(board)
                    copied_board[i][j] = p
                    solved = solve(copied_board)
                    if solved:
                        return solved
                return None
    return board

def p96():
    s = 0
    for board in boards:
        print(board)
        solved = solve(board)
        print(solved)
        s += solved[0][0] * 100 + solved[0][1] * 10 + solved[0][2]
    return s
