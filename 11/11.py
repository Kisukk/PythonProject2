from math import *

for x in range(1, 10000000):
    alf = x
    dlina = 27
    i = ceil(log2(alf))
    v = ceil(dlina * i / 8)
    if 3000000 * v >= 126 * 1024 ** 2:
        print(x)
        break