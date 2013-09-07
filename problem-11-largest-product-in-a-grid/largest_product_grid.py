from os import walk
from copy import copy

def get_grid_file_names_from_dir(directory):
    series_files = []

    for (dirpath, dirnames, filenames) in walk(directory):
        for fname in filenames:
            if fname.endswith("grid"):
                series_files.append(fname)

    return series_files

def grid_file_to_int_grid(fname):
    int_grid = []

    with open(fname, 'r') as f:
        for line_of_digits_and_spaces in f:
            line_of_digits = line_of_digits_and_spaces.rstrip('\n').split(' ')
            actual_digits = map(int, line_of_digits)
            int_grid.append(actual_digits)

    return int_grid

def n_by_n_subgrids_from_int_grid(n, int_grid):
    possible_positions = len(int_grid) - n + 1
    incomplete_subgrids = [[[None for x in range(n)] for y in range(n)] \
        for z in range(possible_positions)]
    complete_subgrids = []

    for y in range(possible_positions):
        for row in range(y, len(int_grid)):
            for x in range(possible_positions):
                subgrid_row = int_grid[row][x:x + n]
                subgrid = incomplete_subgrids[x]
                subgrid[row % n] = subgrid_row[:]

                if row + y % n == n + y - 1:
                    complete_subgrids.append(copy(subgrid))
      
    return complete_subgrids

def find_largest_product_of_n_adjacent_digits_from_grid_files(n, directory):
    prod = lambda xs : reduce(lambda a, x : a*x, xs)
    transpose = lambda two_dim_array : zip(*two_dim_array)
    solutions = []

    for fname in get_grid_file_names_from_dir('.'):
        int_grid = grid_file_to_int_grid(fname)
        subgrids = n_by_n_subgrids_from_int_grid(n, int_grid)

        max_product = 0
    
        for subgrid in subgrids:
            subgrid_transposed = transpose(subgrid)

            for y in range(n):
                row = subgrid[y]
                max_product = max(max_product, prod(row))
                print row

                column = subgrid_transposed[y]
                max_product = max(max_product, prod(column))
                print column

            left_corner_diagonal = [subgrid[i][i] for i in range(n)]
            max_product = max(max_product, prod(left_corner_diagonal))

            right_corner_diagonal = [subgrid[i][n-1-i] for i in range(n)]
            max_product = max(max_product, prod(right_corner_diagonal))

            print left_corner_diagonal, right_corner_diagonal

            exit(1)

        solutions.append(max_product)

    return solutions

print find_largest_product_of_n_adjacent_digits_from_grid_files(4, '.')
