def F(k, x):
    if k <= 49: return x % 2 == 0
    if x == 0: return 0
    h = [F(k - 2, x - 1), F(k - 5, x - 1), F(k // 3, x - 1)]
    return any(h) if x % 2 != 0 else all(h)

print('19', [k for k in range(50,1000) if F(k, 2)])
print('19', [k for k in range(50,1000) if not F(k, 1) and F(k, 3) ])
print('19', [k for k in range(50,1000) if not F(k, 2) and F(k, 4) ])