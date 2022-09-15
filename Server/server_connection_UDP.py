import socket
from threading import Thread


class ServerConnectionUdp:
    def __init__(self):
        ip = "127.0.0.1"
        port = 20001
        self.buffer_size = 1024

        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((ip, port))

    def send(self, message, address):
        bytes_to_send = str.encode(message)
        self.UDPServerSocket.sendto(bytes_to_send, address)

    def listen(self):
        while True:
            bytes_address_pair = self.UDPServerSocket.recvfrom(self.buffer_size)

            message = bytes_address_pair[0]

            address = bytes_address_pair[1]

            client_msg = message.decode()

            print(client_msg)

            if client_msg == "pause":
                message_2 = "video is paused"
                self.send(message_2, address)
            if client_msg == "play":
                message_2 = "video is played"
                self.send(message_2, address)
            if client_msg == "skip":
                message_2 = "video is skipped 5 sec"
                print("send rev")
                self.send(message_2, address)
            if client_msg == "rewind":
                message_2 = "video is rewound 5 sec"
                self.send(message_2, address)


if __name__ == "__main__":
    con_udp = ServerConnectionUdp()

    t1 = Thread(target=con_udp.listen)
    t1.start()
    t1.join()
