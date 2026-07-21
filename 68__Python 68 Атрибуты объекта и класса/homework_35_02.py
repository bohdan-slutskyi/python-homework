""" 02. Проверка данных пользователя

Доработайте класс User.
- Добавьте валидации полей при создании.
- Имя должно быть непустой строкой.
- Пароль должен быть строкой длиной не менее 5 символов.
- Если данные некорректны — выбрасывайте ValueError.
- Добавьте строковое представление объекта.
- Проверьте работу класса с разными значениями.
"""

# Источник: ../materials/theory_01__class_attribute__vs__instance_attribute.md — атрибут класса
# Источник: ../materials/theory_03__classmethod.md — метод класса и cls
# Источник: ../materials/theory_05__str__and__repr__.md — __repr__()

class User:
    total_users = 0

    def __init__(self, username: str, password: str) -> None:
        if not isinstance(username, str) or not username:
            raise ValueError("Username must be a non-empty string.")
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError("Password must be a string with at least 5 characters.")

        self.username = username
        self.password = password
        User.total_users += 1

    def __repr__(self) -> str:
        return f"User(username='{self.username}')"

    @classmethod
    def get_total(cls) -> int:
        return cls.total_users


try:
    user1 = User("alice", "pass123")
    print(user1)  # User(username='alice')
except ValueError as e:
    print("Error:", e)

try:
    user2 = User("", "12345")  # Некорректное имя
except ValueError as e:
    print("Error:", e)

try:
    user3 = User("bob", "123")  # Слишком короткий пароль
except ValueError as e:
    print("Error:", e)

print(f"Total users: {User.get_total()}")
# Должно быть 1, только валидные пользователи считаются


# User(username='alice')
# Error: Username must be a non-empty string.
# Error: Password must be a string with at least 5 characters.
# Total users: 1
