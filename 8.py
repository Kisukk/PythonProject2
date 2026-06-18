from itertools import product
alf = sorted('РЕГИНА')
count = 0
otv = []
for x in product(alf, repeat=5):
    count += 1
    if x.count('Р') == 1 and x.count('Г') == 1 and x.count('Н') <= 1:
        otv.append(x)
print(len(otv))