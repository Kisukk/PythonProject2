
d = list(range(133,178))
b = list(range(144, 191))
a = []
for x in range(200):
    if not( (x in d) <= (((x not in b) and (x not in a)) <= (x not in d))):
        a.append(x)
print(a)
print(a[-1] - a[0] + 1)