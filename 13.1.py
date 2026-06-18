from ipaddress import *

a = ip_network('10.100.202.32/255.255.240.0', 0)
print(a[-2])