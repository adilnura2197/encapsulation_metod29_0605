class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def __init__(self, username, role):
        super().__init__(username)
        self._role = role

    def login(self):
        print("Login successful")

    def ban(self):
        print("User banned")


a1 = Admin("Ali", "superadmin")

a1.login()
a1.ban()
