from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)
@lru_cache(None)
def F(n):
    return 2 * (G(n - 3) + 8)
def G(n):
    if n < 10:
        return n * 2
    else:
        return G(n - 2) + 1
print(F(15548))