import socket
from _thread import *


class ConnectionServer:
    """
    Class for creating a server-to-client connection.
    """
    def __init__(self, host, port):
        self.server_socket = socket.socket()
        try:
            self.server_socket.bind((host, port))
        except socket.error as e:
            print(str(e))
        self.server_socket.listen()

        while True:
            self.accept_connections()

    @staticmethod
    def client_handler(connection):
        """
        Method that keeps the server and client connected
        """
        while True:
            data = connection.recv(2048)
            message = data.decode('utf-8')
            if message == 'END_CONNECTION':
                break
            if message == 'PING':
                connection.send(str.encode("PING"))
        connection.close()

    def accept_connections(self):
        """
        Accepting connections from clients
        """
        client, address = self.server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(self.client_handler, (client,))


if __name__ == "__main__":
    host = ''
    port = 1233

    ConnectionServer(host, port)
