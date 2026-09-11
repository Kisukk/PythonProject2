for K in range(10000):
    digits = [int(x) for x in str(K)]
    s = sum(digits)
    m = max(digits)
    n = min(digits)
    p1 = s - m
    p2 = s - n
    if p1 > p2:
        i = str(p1) + str(p2)
    else:
        i = str(p2) + str(p1)
    if i == '2013':
        print(K)
