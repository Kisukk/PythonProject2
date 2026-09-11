import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def F(n):
    if n == 1:
        return 1
    else:
        return n * F(n - 1)

print(((F(3000) / 150) + F(2999)) / F(2998))