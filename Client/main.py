import settings
from view import View
import connection_client


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


def server_queries(conn: connection_client.ConnectionClient):
    while True:
        View.print_main_lobby_options()
        user_input = input()
        match user_input:
            case "create":
                conn.create_room()
            case "join":
                conn.join_room()
            case "show":
                # TODO Get room list
                pass
            case "end":
                return


def server_connection():
    if not get_connection_info(Settings_manager):
        return
    conn = connection_client.ConnectionClient(Settings_manager.get_IP_address(), Settings_manager.get_port())
    conn.send_nickname()
    server_queries(conn)
    conn.close_connection()


if __name__ == "__main__":
    Settings_manager = settings.Settings()
    Settings_manager.import_settings()
    server_connection()









