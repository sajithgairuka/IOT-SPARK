import socket
import struct
import time

#https://www.py4u.net/discuss/12815
#https://github.com/cabo/coaping/blob/master/bin/coaping

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
msg = 0b01000000
val = 0
def_time = 2
coap_pac = struct.pack('BB',msg,val)
s.settimeout(3)

remoteServer = input("Input Ip range (Ex 192.168.8.) : ")

def pack_mon():
    for ip in range(100,200):
        addr = remoteServer+str(ip)
        s.connect((addr ,5683))
        s.sendto(coap_pac,(addr,5683))
        try:
            m=s.recvfrom(100)
            if m[0]!=None:
                print("This is a coap server : %s | This is a reply : %s" % (addr,m[0]))

        except socket.timeout:
            print("Couldn't connect" ,addr)
            #s.close()


pack_mon()
