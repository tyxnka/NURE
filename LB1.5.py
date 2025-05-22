import hashlib


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


users = {
    "oleg123": (hash_password("qwerty123"), "Попов Олег Александрович"),
    "olga1994": (hash_password("pass456"), "Білокур Ольга Миколаївна"),
    "admin": (hash_password("admin123"), "Адміністратор Системи")
}


def authenticate_user(login):
    if login not in users:
        print("Користувача не знайдено.")
        return False

    password = input("Введіть пароль: ")
    hashed_input = hash_password(password)

    stored_hash, full_name = users[login]
    if hashed_input == stored_hash:
        print(f"Аутентифікація успішна. Ласкаво просимо, {full_name}!")
        return True
    else:
        print("Невірний пароль.")
        return False


login_input = input("Введіть логін: ")
authenticate_user(login_input)
