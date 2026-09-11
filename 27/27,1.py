from math import *
def center(cl):
    best = []
    minsum = 10**9
    for pp in cl:
        summ = sum(dist(pp[:2], pp1[:2])for pp1 in cl)
        if summ < minsum:
            minsum = summ
            best = pp
    return best
def anticenter(cl):
    best = []
    maxsumm= 0
    for pp in cl:
        summ = sum(dist(pp[:2], pp1[:2])for pp1 in cl)
        if summ > maxsumm:
            maxsumm = summ
            best = pp
    return best

cla = [[],[]]
for s in open('27a.txt'):
    s = s.replace(',', '.')
    x,y = s.split()
    x,y = float(x), float(y)
    if y<15 and y>10 and x>0: cla[0].append([x,y])
    elif y>15 and x > 0: cla[1].append([x,y])


clb = [[],[],[]]
for s in open('27b.txt'):
    s = s.replace(',', '.')
    x,y = s.split()
    x,y = float(x), float(y)
    if y>5 and x>-1 and x<0: clb[0].append([x,y])
    elif y < 5 and x>-1: clb[1].append([x,y])
    elif y < 5 and x>-2: clb[2].append([x,y])


#a
cnta0 = center(cla[0])
cnta1 = center(cla[1])

a = dist(cnta0[:1], cnta1[:1])
a1 = dist(cnta0[1:], cnta1[1:])
print(int(a*10000), int(a1*10000))

#b
cntb0 = center(clb[0])
cntb1 = center(clb[1])
cntb2 = center(clb[2])
q1 = dist(cntb0, cntb2)
maxsum = 0




print(int(q1*10000), int((dist(cntb0,anticenter(clb[0]))*10000)))
