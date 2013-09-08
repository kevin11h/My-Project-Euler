from math import sqrt
from sys import argv

def get_nth_triangular_number(n):
    assert n > 0

    triangular_number = 0

    for i in range(1, n+1):
        triangular_number += i

    return triangular_number

def num_divisors(n):
    assert n != 0

    divisors_count = 1

    if n == 1:
        return divisors_count
    else:
        divisors_count += 1

    for d in range(divisors_count, int(sqrt(n))):
        if n % d == 0:
            divisors_count += 2

    if int(sqrt(n))**2 == n:
        divisors_count += 1

    return divisors_count
    
def triangular_number_with_over_d_number_divisors(d):
    assert d >= 0

    if d == 0:
        return get_nth_triangular_number(1)
    else:
        n = 1
        triangular_num = get_nth_triangular_number(n)

        while num_divisors(triangular_num) <= d:
            n += 1
            triangular_num = get_nth_triangular_number(n)

        return triangular_num

print triangular_number_with_over_d_number_divisors(int(argv[1]))
