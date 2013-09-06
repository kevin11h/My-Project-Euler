def evens(xs):
    return filter(lambda x : x % 2 is 0, xs)

def fibonacci_terms_less_than_n(n):
    old_f1 = 0
    f1 = 1
    f2 = 2

    yield f1
    yield f2

    while f1 + f2 < n:
        old_f1 = f1
        f1 = f2
        f2 = old_f1 + f2
        yield f2 

FOUR_MILLION = 4 * 10**6

print sum(evens(fibonacci_terms_less_than_n(FOUR_MILLION)))
