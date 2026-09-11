def F(s, e):
    if s == e: return 1
    if s < e or s==7: return 0
    return F(s-1, e) + F(s-4, e)+F(s//3, e)
print(F(19,13) * F(13,2))