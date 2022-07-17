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

    def ping(self):
        """
        Checking the time before sending and after receiving the reply
        """
        time_1 = datetime.datetime.now()

        self.client_socket.send(str.encode('PING'))
        response = self.client_socket.recv(2048)

        print(response.decode('utf-8'))
        time_2 = datetime.datetime.now()
        print("%s:%s:%s" % (time_1.minute, time_1.second, time_1.microsecond))
        print("%s:%s:%s" % (time_2.minute, time_2.second, time_2.microsecond))

    def close_connection(self):
        """
        Closing the connection to the server.
        """
        self.client_socket.send(str.encode('END_CONNECTION'))
        self.client_socket.close()


host = '127.0.0.1'
port = 1233

conn = ConnectionClient(host, port)

conn.ping()

conn.close_connection()
