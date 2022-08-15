
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
    def print_main_lobby_options():
        print("{create} a room, {join} a room, {show} room list, {end} connection\n> ", end="")

    @staticmethod
    def incorrect_input():
        print("Input was not recognized, try again...")

    @staticmethod
    def ask_for_new_value():
        print("Please input new value:\n> ", end="")

    @staticmethod
    def ask_for_nickname():
        print("Please input your nickname:\n> ", end="")
