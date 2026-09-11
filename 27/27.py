from math import *

def center(cl):
    best = []
    minsum = 10**9
    for p in cl:
        summ = sum(dist(p[:2], p1[:2] ) for p1 in cl)
        if summ < minsum:
            best = p
            minsum = summ
    return best

#A
cla = [[],[]]
for s in open('27a.txt'):
    s = s.replace(',', '.')
    x,y,har = s.split()
    x,y = float(x), float(y)
    if y > 15: cla[0].append([x,y,har])
    else: cla[1].append([x,y,har])

clb = [[],[],[]]
for s in open('27b.txt'):
    s = s.replace(',', '.')
    x,y,har = s.split()
    x,y = float(x), float(y)
    if x > 16: clb[0].append([x,y,har])
    elif y > 30: clb[1].append([x,y,har])
    else: clb[2].append([x,y,har])

#a
cla.sort(key=len)
cnta = center(cla[0])
ansa = []
minr = 10**9
for x,y,har in (cla[0]+cla[1]):
    if har[0]=='M' and har[2:]=='III' and dist([x,y], cnta[:2]) < minr:
        ansa = [x,y]
        minr = dist([x,y], cnta[:2])
ax, ay = ansa
print(int(abs(ax)*10000), int(abs(ay)*10000))

#b
#(len([15 for x,y,har in clb[0] if har[0]=='K' and har[2:]=='III']))
#print(len([15 for x,y,har in clb[15] if har[0]=='K' and har[2:]=='III']))
#print(len([15 for x,y,har in clb[2] if har[0]=='K' and har[2:]=='III']))
b1 = dist(center(clb[0])[:2], center(clb[2])[:2])
b2 = 0
for cl in clb:
    for x1,y1,har1 in cl:
        for x2, y2, har2 in cl:
            if har1[0]==har2[0]=='G' and har1[2:]==har2[2:]=='V':
                b2 = max(b2, dist([x1,y1], [x2,y2]))
print(int(abs(b1)*10000), int(abs(b2)*10000))


