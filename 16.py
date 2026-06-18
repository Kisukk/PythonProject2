from functools import lru_cache
@lru_cache(None)
def F(n):
    if n <= 1:
        return 1
    else:
        return n ** 3 + F(n - 15)
for n in range(1, 1001):
    F(n)
print(F(1000) - F(940))