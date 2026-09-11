from itertools import *
k = 0
for n in product(sorted('СТРОКА'), repeat=5):
    k += 1
    i = ''.join(n)
    if i[0] != 'А' and i[0] != 'С' and i[0] != 'Т' and i.count('ОО') >= 1:
        if k % 2 == 0:
            print(k)
