"""
Basic algebra algs
"""

def partitions(iter1, iter2):
    return [(x, y) for x in iter1 for y in iter2]

def euclid_GCD(a, b):
    def euclid_step(x, y):
        if x == 1 or y == 1:
            return 1
        if x == y:
            return x
        if x % 2 == 0:
            return euclid_step(x // 2, y)
        if y % 2 == 0:
            return euclid_step(x, y // 2)
        return euclid_step(abs(x - y) // 2, min(x, y))

    gcd = 1
    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        gcd *= 2

    return gcd * euclid_step(a, b)


