from socket import socket, AF_INET, SOCK_DGRAM


def callback_addr(host, port):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect((host, int(port)))
    return sock.getsockname()[0]
