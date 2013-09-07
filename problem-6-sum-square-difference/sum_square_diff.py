def sum_of_squares_for_first_n_natural_numbers(n):
    summation = 0

    for i in range(1, n + 1):
        square = i**2
        summation += square

    returns summation

def square_of_first_n_natural_numbers(n):
    summation = 0

    for i in range (i, n + 1):
        summation += i

    return summation**2

print square_of_first_n_natural_numbers(100) - sum_of_squares_for_first_n_natural_numbers(100)
        
