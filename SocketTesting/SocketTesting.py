# !/usr/bin/python3

import socket
try:
    Host_name = socket.gethostname()
    print(Host_name)
    print()
    Host_addr = socket.gethostbyname_ex(Host_name)
    print(Host_addr)
    print()
#    IPv6 = socket.getaddrinfo(Host_name)
#    print(IPv6)
except:
    print('err')