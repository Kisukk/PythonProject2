spisok = []
for N in range(1, 416):
    r = bin(N)[2:]
    if N % 3 == 0:
        r = str(r) + str(r)[-3:]
        if int(r,2) < 416:
            spisok.append(int(r,2))
    else:
        ost = (N % 3 + 1) * 3
        ost = bin(ost)[2:]
        r = str(r) + str(ost)
        if int(r,2) < 416:
            spisok.append(int(r,2))
print(sorted(spisok))