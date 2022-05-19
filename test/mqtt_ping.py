import socket
import sys

remoteServer = input("Input Ip range (Ex 192.168.8.) : ")

def iprange():
    try:
        for ip in range(100,200):
            addr = remoteServer+str(ip)
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((addr,1883))
            if result == 0 :
                print(addr, "this mqtt server")
            else:
                sock.close()

    except socket.error:
        print("Couldn't connect ip range")
        sys.exit()

    except KeyboardInterrupt:
        sys.exit()

iprange()
