def f(x, y):
    return (x < A) and (y < A) and (105 != y + 2*x)

for A in range(1, 500):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(A)
