for i in range(999, 10000):
    a = i // 1000
    d = i % 10
    b = i // 100 % 10
    c = i % 100 // 10
    s1 = int(a) + int(b)
    s2 = int(b) + int(c)
    s3 = int(c) + int(d)
    min1 = min(s1, s2, s3)
    if min1 == s1:
        if str(s2) + str(s3) == '614':
            print(i)
            break
    elif min1 == s2:
        if str(s1) + str(s3) == '614':
            print(i)
            break
    else:
        if str(s1) + str(s3) == '614':
            print(i)
            break