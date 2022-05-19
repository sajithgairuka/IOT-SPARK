from coapthon.client.helperclient import HelperClient

host = "192.168.8.200"
port = 5683

def main():
    client = HelperClient(server=(host, port))
    response = client.get("/.well-known/core")
    print(response.pretty_print())

if __name__ == '__main__':
    main()
