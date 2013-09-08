import sys
sys.path.append('../lib')
from bignatural import BigNatural

def factorial(n, accum):
    if n <= 1:
        return accum
    else:
        return factorial(n - 1, accum * BigNatural(str(n)))

def digits_of_n_factorial(n):
    return factorial(n, BigNatural("1")).digits

print sum(digits_of_n_factorial(100))
