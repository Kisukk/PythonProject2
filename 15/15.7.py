b = list(range(25,41))
c = list(range(12,34))
a = []

for x in range(50):
    if not( ((x in b) <= (x in a)) and ((x not in c) or (x in a)) ):
        a.append(x)
print(a)
print(a[-1] - a[0])