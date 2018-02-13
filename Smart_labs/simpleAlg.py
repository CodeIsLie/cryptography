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


def extended_euclid(a, b):
    if b > a:
        return extended_euclid(b, a)

    s_koef = [0, 1]
    t_koef = [1, 0]
    i = 1
    r = a % b
    r_prev = 0
    q = a // b

    if r == 0:
        return b, 0, 1

    # start from second step
    while r != 0:
        a = b
        b = r

        q_prev = q
        r_prev = r
        r = a % b
        q = a // b
        i += 1

        s_koef.append(s_koef[i - 2] - s_koef[i - 1] * q_prev)
        t_koef.append(t_koef[i - 2] - t_koef[i - 1] * q_prev)

        # print("{0} | {1} | {2} | {3} | {4} | {5}".format(a, b, q, r, s_koef[i], t_koef[i]))

    return r_prev, s_koef[i], t_koef[i]


