count = 0
net = []
chet = []
for n in open('file'):
    a = [int(x) for x in n.split()]
    avg = sum(a)/len(a)
    p2 = [x for x in a if x > avg]
    for x in p2:
        if x % 2 == 0:
            chet.append(x)
        else:
            net.append(x)
    if len(chet) > len(net) and sum(chet) < sum(net):
        count += 1
print(count)


