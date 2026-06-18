from ipaddress import *

a = ip_network('89.16.43.107/255.244.0.0', 0)

print(a[-2])