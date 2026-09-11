def f(x):
    return (x % a == 0) or ((70 <= x <= 90) <= (x % 22 != 0))

for a in range(1,10000):
    if all(f(x) for x in range(1, 1000)):
        print(a)