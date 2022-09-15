import socket
from threading import Thread


class ClientConnectionUdp:
    def __init__(self):
        self.server_address = ("127.0.0.1", 20001)
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.buffer_size = 1024
        ip = "127.0.0.1"
        port = 20040
        self.UDPClientSocket.bind((ip, port))

    def send(self, message):
        bytes_to_send = str.encode(message)
        self.UDPClientSocket.sendto(bytes_to_send, self.server_address)

        msg_from_server = self.UDPClientSocket.recvfrom(self.buffer_size)

        msg = msg_from_server[0].decode()
        print(msg)

    def listen(self):
        while True:
            bytes_address_pair = self.UDPClientSocket.recvfrom(self.buffer_size)
            message_3 = bytes_address_pair[0]

            client_msg = message_3.decode()

            print(client_msg)


def room():
    while True:
        e = input("action")
        if e == "pause":
            message = "pause"
            con_udp.send(message)
        if e == "play":
            message = "play"
            con_udp.send(message)
        if e == "skip":
            message = "skip"
            con_udp.send(message)
        if e == "rewind":
            message = "rewind"
            con_udp.send(message)


if __name__ == "__main__":
    con_udp = ClientConnectionUdp()
    t1 = Thread(target=con_udp.listen)
    t2 = Thread(target=room)
    t1.start()
    t2.start()
    t1.join()
    t2.join()



