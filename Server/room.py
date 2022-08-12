

class Room:
    """
    Room class that stores room data
    """
    def __init__(self, __name_of_room: str, __owner_of_room: str, __checksum: str):
        self.__room_name: str = __name_of_room
        self.__room_owner: str = __owner_of_room
        self.__checksum: str = __checksum
        self.__room_members_list: list[str] = []
        self.__room_members_list.append(self.__room_owner)

    def join_room(self, client_name: str, client_checksum: str):
        """
        Adds a client to the room
        """
        if client_checksum == self.__checksum:
            self.__room_members_list.append(client_name)

    def change_room_owner(self, new_owner):
        """
        Changes the owner of the room
        """
        for user in self.__room_members_list:
            if user == new_owner:
                self.__room_owner = new_owner

    def get_owner(self):
        """
        Get the owner of the room

        :return: room owner
        """
        return self.__room_owner

    def owner_leave(self):
        """
        When the owner leaves the room, it sets another person in the room as the owner
        """
        self.__room_owner = self.__room_members_list[0]

    def show_room(self):
        """
        Displays current room and their data
        """
        print("room name: ", self.__room_name)
        print("room owner: ", self.__room_owner)
        print("room members:", self.__room_members_list)

    def get_room_name(self):
        """
        Get room name

        :return: stored room name
        """
        return self.__room_name

    def number_of_members(self) -> int:
        """
        Checks how many people are in the room

        :return: number of members
        """
        return len(self.__room_members_list)

    def leave_room(self, client_name: str):
        """
        Removes the client from the list of people in the room
        """
        for client in self.__room_members_list:
            if client == client_name:
                self.__room_members_list.remove(client)


