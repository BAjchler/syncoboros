

class Client:
    """
    Client class that stores information about the client
    """
    def __init__(self, nickname: str):
        self.__client_name = nickname
        self.__room_name: str = ""

    def get_client_name(self):
        """
        Get client name

        :return: client name
        """
        return self.__client_name

    def get_room_name(self):
        """
        Get room name

        :return: room name assigned to the client
        """
        return self.__room_name

    def delete_room_name(self):
        """
        Deletes room name
        """
        self.__room_name = ""

    def set_client_name(self, client_name):
        """
        Sets the name of the client
        """
        self.__client_name = client_name

    def join_room(self, room):
        """
        Assigns a room name to the client
        """
        self.__room_name = room
