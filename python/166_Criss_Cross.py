import copy

def print_grid(grid):
    print('\n'.join(' '.join(map(str,row)) for row in grid))
    print()

def gen_grids(grid, row_sums, col_sums, diag_sum, rdiag_sum, N, tot, row, col):
    # print(f'gen_grids({grid}, {row_sums}, {col_sums}, {diag_sum}, {rdiag_sum}, {row}, {col})')
    if row == N - 1 and col == N - 1:
        # finishing the grid
        if tot - row_sums[row] == tot - col_sums[col] == tot - diag_sum:
            d = tot - row_sums[row]
            if 0 <= d < 10:
                new_grid = copy.deepcopy(grid)
                new_grid[row][col] = d
                print_grid(new_grid)
                return 1
    elif col == N - 1:
        # finishing a row
        d = tot - row_sums[row]
        if 0 <= d < 10:
            new_row_sums = row_sums[:]
            new_col_sums = col_sums[:]
            new_row_sums[row] += d
            new_col_sums[col] += d
            if row == col:
                diag_sum += d
            if row == N - col - 1:
                rdiag_sum += d
            new_grid = copy.deepcopy(grid)
            new_grid[row][col] = d
            return gen_grids(new_grid, new_row_sums, new_col_sums, diag_sum, rdiag_sum, N, tot, row + 1, 0)
    elif row == N - 1 and col == 0:
        # finishing first col and the reverse diagonal
        if tot - col_sums[col] == tot - rdiag_sum:
            d = tot - col_sums[col]
            if 0 <= d < 10:
                new_row_sums = row_sums[:]
                new_col_sums = col_sums[:]
                new_row_sums[row] += d
                new_col_sums[col] += d
                if row == col:
                    diag_sum += d
                if row == N - col - 1:
                    rdiag_sum += d
                new_grid = copy.deepcopy(grid)
                new_grid[row][col] = d
                return gen_grids(new_grid, new_row_sums, new_col_sums, diag_sum, rdiag_sum, N, tot, row, col + 1)
    elif row == N - 1:
        # finishing a col
        d = tot - col_sums[col]
        if 0 <= d < 10:
            new_row_sums = row_sums[:]
            new_col_sums = col_sums[:]
            new_row_sums[row] += d
            new_col_sums[col] += d
            if row == col:
                diag_sum += d
            if row == N - col - 1:
                rdiag_sum += d
            new_grid = copy.deepcopy(grid)
            new_grid[row][col] = d
            return gen_grids(new_grid, new_row_sums, new_col_sums, diag_sum, rdiag_sum, N, tot, row, col + 1)
    else:
        # try some options
        max_d = min(tot - row_sums[row], tot - col_sums[col], 9)
        s = 0
        for d in range(0, max_d + 1):
            new_row_sums = row_sums[:]
            new_col_sums = col_sums[:]
            new_row_sums[row] += d
            new_col_sums[col] += d
            new_diag_sum = diag_sum
            new_rdiag_sum = rdiag_sum
            if row == col:
                new_diag_sum += d
            if row == N - col - 1:
                new_rdiag_sum += d
            new_grid = copy.deepcopy(grid)
            new_grid[row][col] = d
            s += gen_grids(new_grid, new_row_sums, new_col_sums, new_diag_sum, new_rdiag_sum, N, tot, row, col + 1)
        return s
    return 0

def gen_grids2(row_sums, col_sums, diag_sum, rdiag_sum, N, tot, row, col):
    if row == N - 1 and col == N - 1:
        # finishing the grid
        if tot - row_sums[row] == tot - col_sums[col] == tot - diag_sum:
            d = tot - row_sums[row]
            if 0 <= d < 10:
                return 1
    elif col == N - 1:
        # finishing a row
        d = tot - row_sums[row]
        if 0 <= d < 10:
            new_row_sums = row_sums[:]
            new_col_sums = col_sums[:]
            new_row_sums[row] += d
            new_col_sums[col] += d
            if row == col:
                diag_sum += d
            if row == N - col - 1:
                rdiag_sum += d
            return gen_grids2(new_row_sums, new_col_sums, diag_sum, rdiag_sum, N, tot, row + 1, 0)
    elif row == N - 1 and col == 0:
        # finishing first col and the reverse diagonal
        if tot - col_sums[col] == tot - rdiag_sum:
            d = tot - col_sums[col]
            if 0 <= d < 10:
                new_row_sums = row_sums[:]
                new_col_sums = col_sums[:]
                new_row_sums[row] += d
                new_col_sums[col] += d
                if row == col:
                    diag_sum += d
                if row == N - col - 1:
                    rdiag_sum += d
                return gen_grids2(new_row_sums, new_col_sums, diag_sum, rdiag_sum, N, tot, row, col + 1)
    elif row == N - 1:
        # finishing a col
        d = tot - col_sums[col]
        if 0 <= d < 10:
            new_row_sums = row_sums[:]
            new_col_sums = col_sums[:]
            new_row_sums[row] += d
            new_col_sums[col] += d
            if row == col:
                diag_sum += d
            if row == N - col - 1:
                rdiag_sum += d
            return gen_grids2(new_row_sums, new_col_sums, diag_sum, rdiag_sum, N, tot, row, col + 1)
    else:
        # try some options
        max_d = min(tot - row_sums[row], tot - col_sums[col], 9)
        s = 0
        for d in range(0, max_d + 1):
            new_row_sums = row_sums[:]
            new_col_sums = col_sums[:]
            new_row_sums[row] += d
            new_col_sums[col] += d
            new_diag_sum = diag_sum
            new_rdiag_sum = rdiag_sum
            if row == col:
                new_diag_sum += d
            if row == N - col - 1:
                new_rdiag_sum += d
            s += gen_grids2(new_row_sums, new_col_sums, new_diag_sum, new_rdiag_sum, N, tot, row, col + 1)
        return s
    return 0

def p166():
    s = 0
    for tot in range(0, 9*4 + 1):
        ngrids = gen_grids2([0] * 4, [0] * 4, 0, 0, 4, tot, 0, 0)
        s += ngrids
        print(tot, ngrids, s)
    return s
