from itertools import *
k = 0
for x in product(sorted('МОСКВА'), repeat=6):
    d = ''.join(x)
    k += 1
    if k % 2 != 0:
        if d[0] != 'А' and d[0] != 'В' and d[0] != 'К' and d.count('М') == 2:
            print(d)
            print(k)