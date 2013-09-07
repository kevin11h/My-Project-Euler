from os import walk

def get_series_file_names_from_dir(directory):
    series_files = []

    for (dirpath, dirnames, filenames) in walk(directory):
        for fname in filenames:
            if fname.endswith("series"):
                series_files.append(fname)

    return series_files

def series_file_to_int_list(fname):
    int_list = []

    with open(fname, 'r') as f:
        for line_of_digits in f:
            int_list.extend(list(line_of_digits.rstrip('\n')))

    return map(int, int_list)

def largest_product_of_n_consecutive_digits(n, digits): 
    return
          
def find_largest_product_n_digit_series(n, directory):
    fnames = get_series_file_names_from_dir(directory)
    solutions = []
    prod = lambda xs : reduce(lambda a, x : a*x, xs)

    for fname in fnames:
        int_list = series_file_to_int_list(fname)

        max_product = 0
        possible_positions = len(int_list) - n + 1

        for i in range(0, possible_positions):
            n_digit_slice = int_list[i:i + n]
            max_product = max(max_product, prod(n_digit_slice))

        solutions.append(max_product)

    return solutions

print find_largest_product_n_digit_series(5, '.')

