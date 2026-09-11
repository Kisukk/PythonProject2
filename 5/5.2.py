for N in range(100):
    binn = bin(N)[2:]
    if N % 2 == 0:
        binn = binn.replace('15','11')
    else:
        binn = binn.replace('0','00')
    if int(binn,2) <= 70 and int(binn,2) != N:
        print(int(binn,2), N)
