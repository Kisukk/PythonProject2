def to_base5(n):
    res = ''
    while n > 0:
        res = str(n % 5) + res
        n //= 5
    return res

for x in range(2735):
    k = 5**2025 + 5 ** 1500 - x
    k = to_base5(k)
    if k.count('0')==527:
        print(x)