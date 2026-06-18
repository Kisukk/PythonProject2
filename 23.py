def F(t, e):
    if t == e: return 1
    if t < e or t == 8: return 0
    return F(t - 1, e) + F(t - 4, e) + F(t // 2, e)
print(F(30, 12) * F(10, 4))