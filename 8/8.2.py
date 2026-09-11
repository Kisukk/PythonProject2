from itertools import *
alph = '0123456'
even = '0246'
count = 0
count1 = 0
for x in product(sorted(alph), repeat=6):
    if x[0] == '0':
        continue
    if x.count('0') != 1:
        continue
    f = x.index('0')
    if f == 5:
        if x[f-1] not in even:
            count += 1
    else:
        if (x[f - 1] not in even) and (x[f+1] not in even):
            count += 1
print(count)

