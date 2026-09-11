p = list(range(15,34))
q = list(range(35,49))
a = list(range(100))
for x in range(100):
    if not( ((x in a) and (x not in q)) <= ((x in p) or (x in q))):
        a.remove(x)
print(a)
print(len(a))
print(a[-1] - a[0])
# надо посчитать максимальную длину тут два отрезка 15-33 35-48
# наибольший 18