from math import *

def center(cl):
    best = []
    minsum = 10**9
    for pp in cl:
        summ = sum(abs(pp[0] - pp1[0]) for pp1 in cl)
        if summ < minsum:
            minsum = summ
            best = pp
    return best
p = []
for s in open('27.txt'):
    s = s.replace(',','.')
    x, y, vx, vy, m, har = s.split()
    x, y, vx, vy, m = float(x), float(y), float(vx), float(vy), float(m)
    e = 1/2*m*(vx**2+vy**2)
    p.append([e, x, y, har])

p.sort()
cla = [[p[0]]]
for p1 in p[1:]:
    if p1[0] - cla[-1][0][0]<=2: cla[-1].append(p1)
    else: cla.append([p1])

dists = []
for cl in cla:
    for i in range(len(cl)):
        for j in range(i+1, len(cl)):
            if cl[i][3]==cl[j][3]=='II':
                dists.append(dist(cl[i][1:3], cl[j][1:3]))
q1 = max(dists)

cnt = [center(cl) for cl in cla]
q2 = max(pp[0] for pp in cnt)
print(int(q1*10000), int(q2*10000))


