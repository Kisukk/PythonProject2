from ipaddress import *

a = ip_network('200.33.100.0/255.255.248.0', 0)
k = 0
for ipa in a:
    b = ipa
    b = bin(int(b))[2:]
    ff = b.count('1')
    if ff % 7 != 0:
        k = k + 1



print(k)
