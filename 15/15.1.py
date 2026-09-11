#https://www.youtube.com/watch?v=v3OiJ0Zywjw

def f(x, y):
    return (x - 3*y < a) or (y > 400) or (x > 56)
for a in range(0,500):
    if all(f(x,y ) for x in range(1,1000) for y in range(1,1000)):
        print(a)
        break