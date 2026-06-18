from itertools import product
alf = sorted('СТРЕЛА')
count = 0
otv = []
for x in product(alf, repeat=5):
    count+=1
    if x.count('Е') == 2 and 'ЕЕ' not in x and x[:1] != "А" and x[:1] != 'С' and x[:1] != 'Т':
        otv.append(x)
print(otv)