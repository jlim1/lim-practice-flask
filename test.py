import socket


def get_ip_address():
    # Resolve the loopback name rather than displaying the machine's address.
    return socket.gethostbyname("localhost")


if __name__ == "__main__":
    print(get_ip_address())
