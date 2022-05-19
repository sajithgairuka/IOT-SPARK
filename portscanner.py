import socket
import sys

remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)


try:
    for port in range(1,65533):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect")
    sys.exit()
