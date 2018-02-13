"""
Basic algebra algs
"""

from math import ceil, floor, sqrt
from functools import reduce

def partitions(iter1, iter2):
    return [(x, y) for x in iter1 for y in iter2]

def product(iter):
    return reduce(lambda x, y: x* y, iter, 1)

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

def get_dividers(x):
    dividers = []
    for i in range(2, round(sqrt(x)) + 1):
        degree = 0
        while x % i == 0:
            degree += 1
            x /= i
        if degree % 2 == 1:
            dividers.append(i)
        if x == 1:
            break
    return dividers

def legandr(a, p):
    if a == 1:
        return 1
    if a == 2:
        return 1 if (p % 8) in (1, 7) else -1
    #if a == -1:
    #    return (2)
    if a > p:
        return legandr(a % p, p)

    dividers = get_dividers(a)
    if len(dividers) == 1:
        return legandr(p, a) * -1 if p % 4 == 3 and a % 4 == 3 else 1
    return product([legandr(div, p) for div in dividers])


def extended_euclid(a, n):
    return None


