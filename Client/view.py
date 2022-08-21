from user import State


class View:

    @staticmethod
    def print_default_settings(settings: dict):
        print("These are your current settings:\n")
        for key, value in settings.items():
            print(f'{key}: {value}')
        print("\nc - connect, d - restore default, i - change IP, p - change port number,"
              " e - exit")
        print("> ", end="")

    @staticmethod
    def print_current_options(state: State):
        match state:
            case State.LOBBY:
                print("{create} a room, {join} a room, {show} room list, {end} connection\n> ", end="")

            case State.ROOM_NOT_PLAYING:
                print("{show} members and their status, {leave} current room, "
                      "{give} host permissions, {start} the video, {select} new video, {join} other room, "
                      "{end} connection\n> ", end="")

            case State.ROOM_PLAYING:
                print("{show} members and their status, {leave} current room, "
                      "{give} host permissions, {stop} the video\n> ", end="")
                pass

    @staticmethod
    def incorrect_input():
        print("Input was not recognized, try again...")

    @staticmethod
    def ask_for_new_value():
        print("Please input new value:\n> ", end="")

    @staticmethod
    def ask_for_nickname():
        print("Please input your nickname:\n> ", end="")

    @staticmethod
    def print_rooms(rooms: list[dict]):
        for room in rooms:
            print(f'Room name: {room.get("room name")}, room owner: {room.get("room owner")}, room members: {room.get("room members")}')

    @staticmethod
    def print_delay(delay: int):
        print(f'Delay between client and server is approximately {delay} milliseconds.')
