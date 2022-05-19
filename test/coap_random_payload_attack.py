import socket
import sys
import random
import string

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

client = None

def client_callback(response):
    print("Callback")

def main():  # pragma: no cover
    global client
    op = "POST"
    path = "coap://192.168.8.113:5683/light"
    payload_len = 1
    #payload = ''.join((random.choice(string.digits) for i in range(1)))

    if path is None:
        print("Path must be specified")
        sys.exit(2)

    if not path.startswith("coap://"):
        print("Path must be conform to coap://host[:port]/path")
        sys.exit(2)

    host, port, path = parse_uri(path)
    try:
        tmp = socket.gethostbyname(host)
        host = tmp
    except socket.gaierror:
        pass
    client = HelperClient(server=(host, port))

    if op == "POST":
        if path is None:
            print("Path cannot be empty for a POST request")
            sys.exit(2)

        while True:
            payload = ''.join((random.choice(string.digits) for i in range(payload_len)))
            response = client.post(path, payload)
            print(response.pretty_print())
            print("Random payload is :" ,payload)
            #client.stop()
    else:
        print("Operation not recognized")
        sys.exit(2)

main()
