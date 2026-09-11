# ОТРЕЗОК ВСЕГДА МЕЖДУ ТОЧКАМИ ИЗ УСЛОВИЯ
# ЕСЛИ ПРОСЯТ МИН ОТРЕЗОК -- НАЧИНАЕМ С ПУСТОГО
# ЕСЛИ ПРОСЯТ МАКС ОТРЕЗОК --- НАЧИНАЕМ С ПОЛНОГО
#

p = list(range(25,65))
q = list(range(40,116))
a = []
for x in range(200):
    if not( (x in p) <= (((x in q) and (x not in a)) <= (x not in p)) ):
        a.append(x)
print(a)
print(len(a))
print(a[-1]-a[0])

