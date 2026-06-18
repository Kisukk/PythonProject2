from functools import lru_cache
@lru_cache(None)
def F(n):
    if n == 1: return 15
    elif n >= 2:
        return 2 * F(n - 1) - n
for n in range(1, 2024):
    F(n)
print((F(2025) - F(2023) - 2) / 2**2022)