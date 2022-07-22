import json


class Settings:

    def __init__(self):
        self.__DEFAULT_SETTINGS = {
            "IP_address": "127.0.0.1",
            "port": "1233",
            "nickname": "default"
        }
        self.__settings = None

    def get_default_settings(self):
        return self.__DEFAULT_SETTINGS

    def get_current_settings(self):
        return self.__settings

    def set_current_settings(self, new_settings: dict):
        self.__settings = new_settings

    def get_IP_address(self):
        return self.__settings["IP_address"]

    def set_IP_address(self, new_ip_address: str):
        self.__settings["IP_address"] = new_ip_address

    def get_port(self):
        return self.__settings["port"]

    def set_port(self, new_port: str):
        if new_port.isnumeric() and 0 < int(new_port) < 65536:
            self.__settings["port"] = new_port
        else:
            raise Exception("Port contains illegal characters or is out of range")

    def get_nickname(self):
        return self.__settings["nickname"]

    def set_nickname(self, new_nickname):
        self.__settings["nickname"] = new_nickname

    def change_setting(self, key, value):
        self.__settings[key] = value

    def update_settings(self, key, value):
        with open("settings.json", 'w') as settings_file:
            self.change_setting(key, value)
            json.dump(self.get_current_settings(), settings_file)

    def create_settings(self):
        with open("settings.json", "w") as settings_file:
            json.dump(self.get_default_settings(), settings_file)

    def import_settings(self):
        try:
            with open("settings.json") as settings_file:
                self.set_current_settings(json.load(settings_file))
        except (FileNotFoundError, json.JSONDecodeError):
            self.create_settings()
            with open("settings.json") as settings_file:
                self.set_current_settings(json.load(settings_file))
