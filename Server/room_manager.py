from time import sleep

from Server.room import Room


class RoomManager:
    """
    RoomManager class stores a list of rooms and clients on the server
    """
    def __init__(self):
        self.__rooms = []
        self.__clients = []

    def add_room(self, room: Room):
        """
        Adds room to the list
        """
        self.__rooms.append(room)

    def delete_room(self, name: str):
        """
        Removes a room from the list
        """
        for i in range(len(self.__rooms)):
            if self.__rooms[i].get_room_name() == name:
                self.__rooms.pop(i)

    def get_room(self, room_name: str) -> Room:
        """
        Get indicated room on the list

        :return: Room class object
        """
        for room in self.__rooms:
            if room.get_room_name() == room_name:
                return room

    def check_room_name(self, room_name):
        """
        Checks if the room name is available

        :return: False if the name is unavailable or True if the name is available
        """
        for room in self.__rooms:
            if room.get_room_name() == room_name:
                return False
        return True

    def show_rooms(self):
        """
        Prints data for all available rooms
        """
        while True:
            sleep(5)
            print("rooms:")
            for room in self.__rooms:
                room.show_room()

    def get_rooms_data(self):
        all_rooms = list()
        for room in self.__rooms:
            all_rooms.append(room.get_room_data())
        return all_rooms

    def add_client(self, client_name):
        """
        Adds a client to the list
        """
        self.__clients.append(client_name)

    def check_client(self, client_name):
        """
        Checks for client name availability

        :return: False if it is unavailable or True if it is available
        """
        for client in self.__clients:
            if client == client_name:
                return False
        return True

    def delete_client(self, client_name):
        """
        Removes the client from the list
        """
        self.__clients.remove(client_name)
