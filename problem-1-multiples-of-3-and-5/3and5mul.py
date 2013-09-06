def sum_of_factors_under_n(factors, n):

    multiples = set([])

    count_x = 0

    for f in factors:
        for x in range(f, n, f):
            multiples.add(x)

    return sum(multiples)

print sum_of_factors_under_n([5,3], 1000)
