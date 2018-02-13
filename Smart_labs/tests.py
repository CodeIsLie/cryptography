from simpleAlg import *


narr1 = [1, 2, 3, 5, 7, 9]
narr2 = [2, 4, 6, 8, 10]
"""
for x, y in partitions(narr1, narr2):
    print("GCD({1}, {2}) = {0}".format(euclid_GCD(x, y), x, y))



leg1 = [1, 2, 3, 4, 5, 6, 7]
leg2 = [3, 5, 7, 11, 13, 19]

for y, x in partitions(leg2, leg1):
    print("({1}/{2}) = {0}".format(legandr(x, y), x, y))
"""


a = 24
b = 13

d = extended_euclid(a, b)
print(d)

print(a * d[2] + b * d[1])