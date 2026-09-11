b = list(range(36,76))
c = list(range(60,111))
a = []
for x in range(200):
    if not( ((x not in a) <= ((x in b) == (x in c))) ):
        a.append(x)
print(a)
print(len(a))
print(a[-1] - a[0])