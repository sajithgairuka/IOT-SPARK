import subprocess
import sys

try:
    for ping in range(1,254):
        address = "192.168.8." + str(ping)
        res = subprocess.call(['ping', '-c', '1', address])
        if res == 0:
            print( "ping to", address, "OK")

except:
    sys.exit()
