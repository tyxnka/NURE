import hashlib
from datetime import datetime

class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.is_active = is_active

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == self._hash_password(password)

    def __str__(self):
        return f"{self.__class__.__name__}({self.username})"


class Administrator(User):
    def __init__(self, username, password, permissions=None):
        super().__init__(username, password)
        self.permissions = permissions if permissions else []

    def add_permission(self, permission):
        self.permissions.append(permission)


class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.last_login = None

    def update_login_time(self):
        self.last_login = datetime.now()


class GuestUser(User):
    def __init__(self, username="guest"):
        super().__init__(username, password="", is_active=False)


class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password):
            print(f"Успішна аутентифікація: {user}")
            if isinstance(user, RegularUser):
                user.update_login_time()
            return user
        print("Невдала аутентифікація")
        return None


if __name__ == "__main__":
    ac = AccessControl()

    admin = Administrator("admin", "admin123", permissions=["add_user", "delete_user"])
    user = RegularUser("john", "pass123")
    guest = GuestUser()

    ac.add_user(admin)
    ac.add_user(user)
    ac.add_user(guest)

    ac.authenticate_user("admin", "admin123")
    ac.authenticate_user("john", "pass123")
    ac.authenticate_user("john", "wrongpass")
    ac.authenticate_user("guest", "")
