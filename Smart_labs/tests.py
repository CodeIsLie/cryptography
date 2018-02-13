from simpleAlg import *


narr1 = [1, 2, 3, 5, 7, 9]
narr2 = [2, 4, 6, 8, 10]

for x, y in partitions(narr1, narr2):
    print("GCD({1}, {2}) = {0}".format(euclid_GCD(x, y), x, y))