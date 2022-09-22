import socket
import datetime
from threading import Thread

from Client.client_connection_UDP import ClientConnectionUdp


class ConnectionClient:
    """
    Class for creating a client-to-server connection.
    """

    def __init__(self, host, port):

        self.client_socket = socket.socket()
        try:
            self.client_socket.connect((host, port))
        except socket.error as e:
            print(str(e))
        self.nickname = ""

    def send_nickname(self):
        """
        Sends the client name to the server
        """
        while True:
            self.nickname = input("pleas input your nickname")
            self.client_socket.send(str.encode(self.nickname))

            res = self.client_socket.recv(2048)
            response = res.decode('utf-8')
            print(response)
            if response == "your nickname is set":
                return self.nickname

    def ping(self):
        """
        Calculates delay between the client and server
        """
        time_1 = datetime.datetime.now()

        self.client_socket.send(str.encode('PING'))
        response = self.client_socket.recv(2048)

        print(response.decode('utf-8'))
        time_2 = datetime.datetime.now()
        print("%s:%s:%s" % (time_1.minute, time_1.second, time_1.microsecond))
        print("%s:%s:%s" % (time_2.minute, time_2.second, time_2.microsecond))

    def create_room(self):
        """
        Sends a request to the server to create a room and sends the data needed
        """
        self.client_socket.send(str.encode('CREATE_ROOM'))
        while True:
            response = self.client_socket.recv(2048)
            res = response.decode('utf-8')
            if res == 'SEND_ROOM_NAME':
                i = input("please input room name")
                self.client_socket.send(str.encode(i))
            elif res == 'SEND_CHECKSUM':
                self.client_socket.send(str.encode('7s7'))
            elif res == "room created successfully":
                print(res)
                break
            else:
                print(res)

    def join_room(self):
        """
        Sends a request to the server to join the room and transmits the data needed
        """
        self.client_socket.send(str.encode('JOIN_ROOM'))
        while True:
            response = self.client_socket.recv(2048)
            res = response.decode('utf-8')
            if res == 'SEND_ROOM_NAME':
                i = input("please input room name")
                self.client_socket.send(str.encode(i))
            elif res == 'SEND_CHECKSUM':
                self.client_socket.send(str.encode('7s7'))
            else:
                print(res)
                break

    def change_owner(self):
        """
        Sends a request to the server to change the room owner
        """
        self.client_socket.send(str.encode('CHANGE_OWNER'))
        i = input("please select new owner")
        self.client_socket.send(str.encode(i))
        response = self.client_socket.recv(2048)
        res = response.decode('utf-8')
        print(res)

    def close_connection(self):
        """
        Closing the connection to the server.
        """
        self.client_socket.send(str.encode('END_CONNECTION'))
        self.client_socket.close()


def room(conn_tcp, conn_udp):
    if_room: bool = False
    nickname = conn.send_nickname()
    conn.ping()

    while True:
        e = input()
        if e == "create":
            conn_tcp.create_room()
            if_room = True
        if e == "join":
            conn_tcp.join_room()
            if_room = True
        if e == "change":
            conn_tcp.change_owner()
        if e == "end":
            break
        if e == "pause" and if_room:
            message = "pause"
            conn_udp.send(nickname + "\n" + message)
        if e == "play" and if_room:
            message = "play"
            conn_udp.send(nickname + "\n" + message)
        if e == "skip" and if_room:
            message = "skip"
            conn_udp.send(nickname + "\n" + message)
        if e == "rewind" and if_room:
            message = "rewind"
            conn_udp.send(nickname + "\n" + message)


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 1233

    conn = ConnectionClient(host, port)
    con_udp = ClientConnectionUdp()
    t1 = Thread(target=con_udp.listen)
    t2 = Thread(target=room, args=(conn, con_udp))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    conn.close_connection()
