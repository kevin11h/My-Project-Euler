# assert n is positive
def collatz_sequence(n):
    yield n

    while n > 1:
        if n % 2 is 0:
            n = n/2
        else:
            n = 3*n + 1

        yield n

def longest_collatz_sequence_under_x(x):
    longest_sequence = 0

    for i in range(x - 1, 0, -1):
        local_length = 0

        for _ in collatz_sequence(i):
            local_length += 1

        longest_sequence = max(longest_sequence, local_length)

    return longest_sequence
    

ONE_MILLION = 10**6
print longest_collatz_sequence_under_x(ONE_MILLION)

