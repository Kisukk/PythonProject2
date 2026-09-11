for n in range(1000):
    binn = bin(n)[2:]
    if n % 3 == 0:
        binn = str(binn) + str(binn[-3:])
    else:
        binn = str(binn) + str(bin(n % 3 * 3)[2:])
    if int(binn, 2) > 200:
        print(n)
        break