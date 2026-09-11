c = list(range(48,95))
j = list(range(83,101))
a = list(range(0,200))

for x in range(200):
    if not( (not((x in c) or (x in j))) <= (x not in a)):
        a.remove(x)
print(a)
print(len(a)) # проверка на дыры
print(a[-1] - a[0])