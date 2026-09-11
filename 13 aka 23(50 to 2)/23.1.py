def F(s, e):
    if s == e: return 1
    if s < e: return 0
    return F(s - 2, e) + F(s // 2, e)
print(F(52, 14)*F(14,2))