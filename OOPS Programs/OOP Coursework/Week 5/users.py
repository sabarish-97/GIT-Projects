class User:                # added class user with attributes
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User: {self.username}"

class Owner(User):         # added class Owner inheriting from user
    def __init__(self, username):
        super().__init__(username)

    def __str__(self):
        return f"Owner: {self.username}"