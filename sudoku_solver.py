def is_valid(grid, r, c, k):
    not_in_row = k not in grid[r]
    not_in_column = k not in [grid[i][c] for i in range(9)]
    not_in_box = k not in [grid[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3) for j in
                           range(c // 3 * 3, c // 3 * 3 + 3)]
    return not_in_row and not_in_column and not_in_box


def solve(grid, r=0, c=0):
    if r == 9:
        yield [row[:] for row in grid] # yield a copy of the grid as a solution
    elif c == 9:
        yield from solve(grid, r + 1, 0)
    elif grid[r][c] != 0:
        yield from solve(grid, r, c + 1)
    else:
        for k in range(1, 10):
            if is_valid(grid, r, c, k):
                grid[r][c] = k
                yield from solve(grid, r, c + 1)
                grid[r][c] = 0 # empty the cell to try again later if the number is not valid


grid = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]
] # placeholder for now, most likely will make it take sudoku puzzles from the web to solve them

for solution in solve([row[:] for row in grid]):
    print('-' * 27)
    print(*solution, sep='\n')
    print('-' * 27)
