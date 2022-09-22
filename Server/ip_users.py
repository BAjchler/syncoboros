
class IpUsers:
    def __init__(self):
        self.users = dict()

    def add_user(self, user_name, ip_user):
        self.users[user_name] = ip_user

    def delete_user(self, user_name):
        self.users.pop(user_name)

    def check_user(self, user_name):
        return self.users[user_name]
