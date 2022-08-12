import socket
import datetime


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

    def send_nickname(self):
        """
        Sends the client name to the server
        """
        while True:
            nickname = input("pleas input your nickname")
            self.client_socket.send(str.encode(nickname))

            res = self.client_socket.recv(2048)
            response = res.decode('utf-8')
            print(response)
            if response == "your nickname is set":
                break

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


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 1233

    conn = ConnectionClient(host, port)
    conn.send_nickname()
    conn.ping()

    while True:
        e = input()
        if e == "create":
            conn.create_room()
        if e == "join":
            conn.join_room()
        if e == "change":
            conn.change_owner()
        if e == "end":
            break
    conn.close_connection()
