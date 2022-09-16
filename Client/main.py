import settings
from view import View
import connection_client
from user import *


def get_connection_info(settings_manager: settings.Settings):
    while True:
        View.print_default_settings(settings_manager.get_current_settings())
        user_input = input()
        match user_input:
            case 'i':
                View.ask_for_new_value()
                new_ip = input()
                settings_manager.set_IP_address(new_ip)
            case 'p':
                View.ask_for_new_value()
                new_port = input()
                try:
                    settings_manager.set_port(new_port)
                except Exception as e:
                    print(e)
            case 'd':
                settings_manager.create_settings()
                settings_manager.import_settings()
            case 'c':
                return True
            case 'e':
                return False
            case _:
                View.incorrect_input()
        settings_manager.update_settings()


def lobby_options(conn: connection_client.ConnectionClient, user_input: str, user: User):
    match user_input:
        case "create":
            user.set_state(State.LOBBY)
            if conn.create_room():
                user.set_state(State.ROOM_NOT_PLAYING)
        case "join":
            user.set_state(State.LOBBY)
            if conn.join_room():
                user.set_state(State.ROOM_NOT_PLAYING)
        case "show":
            conn.show_rooms()
        case "ping":
            conn.ping()
        case "end":
            return False
    return True


def room_options(conn: connection_client.ConnectionClient, user_input: str, user: User):
    match user_input:
        case "create":
            user.set_state(State.LOBBY)
            if conn.create_room():
                user.set_state(State.ROOM_NOT_PLAYING)
        case "join":
            user.set_state(State.LOBBY)
            if conn.join_room():
                user.set_state(State.ROOM_NOT_PLAYING)
        case "leave":
            user.set_state(State.LOBBY)
            conn.leave_room()
        case "show":
            pass
            # TODO: PRINT CURRENT ROOM
        case "end":
            return False
    return True


def server_queries(conn: connection_client.ConnectionClient, user: User):
    while True:
        View.print_current_options(user.get_state())
        user_input = input()
        match user.get_state():
            case State.LOBBY:
                if not lobby_options(conn, user_input, user):
                    return
            case State.ROOM_NOT_PLAYING:
                if not room_options(conn, user_input, user):
                    return
            case State.ROOM_PLAYING:
                pass


def server_connection():
    if not get_connection_info(Settings_manager):
        return
    conn = connection_client.ConnectionClient(Settings_manager.get_IP_address(), Settings_manager.get_port())
    nickname = conn.send_nickname()
    user = User(nickname)
    server_queries(conn, user)
    conn.close_connection()


if __name__ == "__main__":
    Settings_manager = settings.Settings()
    Settings_manager.import_settings()
    server_connection()









