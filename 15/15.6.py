# отрезки
p = list(range(66,68))
o = list(range(32,126))
t = list(range(30,492))
a = []
for x in range(500):
    if not( (x not in a) <= ((x in p) or (x not in o) or (x not in t))):
        a.append(x)
print(a[-1] - a[0])