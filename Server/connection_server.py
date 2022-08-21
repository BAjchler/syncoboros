import socket
from _thread import *
from threading import Thread
import json

from Server.client import Client
from Server.room import Room
from Server.room_manager import RoomManager


class ConnectionServer:
    """
    Class for creating a server-to-client connection.
    """

    def __init__(self, host, port):
        self.server_socket = socket.socket()
        self.room_manager = RoomManager()
        try:
            self.server_socket.bind((host, port))
        except socket.error as e:
            print(str(e))
        self.server_socket.listen()

        t1 = Thread(target=self.room_manager.show_rooms)
        t2 = Thread(target=self.accept_connections)
        t1.start()
        t2.start()

        t1.join()
        t2.join()

    def retrieve_client_name(self, connection):
        """
        Retrieves the name from the client

        :return: client name
        """
        while True:
            room_data = connection.recv(2048)
            nickname = room_data.decode('utf-8')
            if self.room_manager.check_client(nickname):
                self.room_manager.add_client(nickname)
                self.send_response(connection, "your nickname is set")
                break
            self.send_response(connection, "this nickname is not available")
        return nickname

    @staticmethod
    def retrieve_data(connection):
        """
        Retrieves the data from the client needed to create or join a room

        :return: retrieve client data
        """
        connection.send(str.encode("SEND_ROOM_NAME"))
        room_data = connection.recv(2048)
        room_name = room_data.decode('utf-8')

        connection.send(str.encode("SEND_CHECKSUM"))
        room_data = connection.recv(2048)
        room_checksum = room_data.decode('utf-8')
        return room_name, room_checksum

    @staticmethod
    def send_response(connection, message: str):
        """
        Sends a reply to the client
        """
        connection.send(str.encode(message))

    def create_room(self, connection, client: Client):
        """
        Creates room
        """
        while True:
            room_name, room_checksum = self.retrieve_data(connection)

            if self.room_manager.check_room_name(room_name):
                client.join_room(room_name)
                room = Room(room_name, client.get_client_name(), room_checksum)
                self.room_manager.add_room(room)
                self.send_response(connection, "room created successfully")
                break
            else:
                self.send_response(connection, "room name is not available")

    def join_room(self, connection, client: Client):
        """
        Allows the client to join the room
        """
        room_name, room_checksum = self.retrieve_data(connection)
        if not self.room_manager.check_room_name(room_name):
            client.join_room(room_name)
            if self.room_manager.get_room(room_name).join_room(client.get_client_name(), room_checksum):
                self.send_response(connection, "joined room successfully")
            else:
                self.send_response(connection, "incorrect checksum")
        else:
            self.send_response(connection, "room has not been found")

    def change_room_owner(self, room_name, new_owner):
        """
        Changes the owner of the room
        """
        self.room_manager.get_room(room_name).change_room_owner(new_owner)

    def client_leave(self, client: Client):
        """
        Removes the client from the room
        Passes host privileges to another user, if the leaving user is the current room owner
        Closes the room if it is empty
        """
        if client.get_room_name() != "":
            self.room_manager.get_room(client.get_room_name()).leave_room(client.get_client_name())

            if self.room_manager.get_room(client.get_room_name()).number_of_members() == 0:
                self.room_manager.delete_room(client.get_room_name())
            else:
                if client.get_client_name() == self.room_manager.get_room(client.get_room_name()).get_owner():
                    self.room_manager.get_room(client.get_room_name()).owner_leave()
            client.delete_room_name()

    def show_rooms(self, connection):
        data = str.encode(json.dumps(self.room_manager.get_rooms_data()))
        self.send_response(connection, str(len(data)))
        connection.sendall(data)

    def client_handler(self, connection):
        """
        Method that keeps the server and client connected
        """
        nickname = self.retrieve_client_name(connection)
        client = Client(nickname)
        while True:
            data = connection.recv(2048)
            message = data.decode('utf-8')

            if message == 'PING':
                connection.send(str.encode("PING"))

            elif message == 'CREATE_ROOM':
                self.client_leave(client)
                self.create_room(connection, client)

            elif message == 'JOIN_ROOM':
                self.client_leave(client)
                self.join_room(connection, client)

            elif message == 'LEAVE_ROOM':
                self.client_leave(client)

            elif message == 'SHOW_ROOMS':
                self.show_rooms(connection)

            elif message == "CHANGE_OWNER":
                data = connection.recv(2048)
                new_owner = data.decode('utf-8')
                if not client.get_room_name() == "" and client.get_client_name() == self.room_manager.get_room(client.get_room_name()).get_owner():
                    self.change_room_owner(client.get_room_name(), new_owner)
                    self.send_response(connection, "changed room owner")

                else:
                    self.send_response(connection, "did not change room owner")

            elif message == 'END_CONNECTION':
                self.client_leave(client)
                break
        self.room_manager.delete_client(client.get_client_name())
        connection.close()

    def accept_connections(self):
        """
        Accepting connections from clients
        """
        while True:
            client, address = self.server_socket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.client_handler, (client,))


if __name__ == "__main__":
    host = ''
    port = 1233
    ConnectionServer(host, port)
