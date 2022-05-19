import socket
import sys

from coapthon.client.helperclient import HelperClient

host = "192.168.8.113"
port = 5683

def main():  # pragma: no cover
    client = HelperClient(server=(host, port))
    response = client.discover()
    print(response.pretty_print())
    client.stop()

if __name__ == '__main__':
    main()
