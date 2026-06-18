sortesda = []
for n in range(1, 416):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = str(r) + str(r[-3:])
        sortesda.append(int(r, 2))
    elif n % 3 != 0:
        ost = ((n % 3) - 1) * 3
        ost = bin(ost)[2:]
        r = str(r) + str(ost)
        sortesda.append(int(r, 2))
    if int(r, 2) < 416:
        print(int(r, 2))
print(sorted(sortesda))