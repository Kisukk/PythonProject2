from functools import *
from sys import *
setrecursionlimit(1000000)


@lru_cache(maxsize=None)
def f(n):
    if n >= 19: return f(n-4)+3580
    elif n < 19: return 6 * (g(n - 7) - 36)


def g(n):
    if n >= 248045: return n / 20 + 28
    else: return g(n + 9) - 4

print(f(673))