def get_a(b, c):
    return 1000 - b - c

def satisfies_pythagorean_theorem_and_linear_constraints(b, c):
    # a = 1000 - b - c
    # (1000 - b - c)^2 + b^2 = c^2
    # (b^2 + 2bc - 2000b + c^2 - 2000c + 1000^2) + b^2 = c^2
    # 2b^2 + 2bc - 2000b - 2000c + 1000^2 = 0
    # 2b(b + c) - 2000(b + c) + 1000^2 = 0
    # 2(b - 1000)(b + c) + 1000^2 = 0
    return 2*(b - 1000)*(b + c) + 1000000 == 0

def get_b_and_c():
    for b in range(1, 1000):
        for c in range(1, 1000):
            if b < c:
                yield (b, c)

def find_pythagorean_triplet_satisfying_constraints():
    for (b, c) in get_b_and_c():
        if satisfies_pythagorean_theorem_and_linear_constraints(b, c):
            return get_a(b, c), b, c

(a, b, c) = find_pythagorean_triplet_satisfying_constraints()
print a * b * c
