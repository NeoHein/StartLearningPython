import socket
try:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    Host_name = socket.gethostname()
    print(Host_name)
    for port_add in range(0, 80):
#        Host_name = socket.gethostname()
#        print(Host_name)
        result = socket_obj.connect_ex(('192.168.43.192', port_add))
        if result == 0:
            print("The IP Address", "192.168.43.192", "is exits at port:", port_add)
#        socket_obj.close()
        else:
            print("The IP Address is not Active!")
#        socket_obj.close()
except:
    print("err")
    socket_obj.close()
