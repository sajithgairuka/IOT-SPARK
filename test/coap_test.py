import socket
import sys
#import logging

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri
#logging.basicConfig(level=logging.INFO)

client = None


def client_callback(response):
    print("Callback")


def main():  # pragma: no cover
    global client
    op = "POST"
    path = "coap://192.168.8.113:5683/light"
    payload = "1"

    if op is None:
        print("Operation must be specified")
        sys.exit(2)

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
    if op == "GET":
        if path is None:
            print("Path cannot be empty for a GET request")
            sys.exit(2)
        print(path)
        print(host)
        print(port)
        response = client.get(path)
        print(response.pretty_print())
        client.stop()

    elif op == "POST":
        if path is None:
            print("Path cannot be empty for a POST request")
            sys.exit(2)

        if payload is None:
            print("Payload cannot be empty for a POST request")
            sys.exit(2)
        response = client.post(path, payload)
        print(response.pretty_print())
        client.stop()

    elif op == "PUT":
        if path is None:
            print("Path cannot be empty for a PUT request")
            sys.exit(2)
        if payload is None:
            print("Payload cannot be empty for a PUT request")
            sys.exit(2)
        response = client.put(path, payload)
        print(response.pretty_print())
        client.stop()

    else:
        print("Operation not recognized")
        sys.exit(2)


if __name__ == '__main__':  # pragma: no cover
    main()
