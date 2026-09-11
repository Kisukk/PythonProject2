p = {3,6,9,12}
q = {1,2,3,4,5,6}
a = set()
for x in range(200):
    if not( (not((x not in a) and (x in p))) or (x not in q)  ):
        a.add(x)
print(a)