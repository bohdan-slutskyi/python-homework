"""Домашнее задание 32.3: рамка вокруг вывода функции."""

from typing import Callable


# Источник: ../../python-course/62__Python 62 Вложенные функции. Замыкание/materials/theory_02__Enclosing_scope.md — вложенная функция получает доступ к func
def frame(func: Callable[[], None]) -> Callable[[], None]:
    """Добавить строки рамки до и после вызова функции."""

    def wrapper() -> None:
        print("-" * 50)
        func()
        print("-" * 50)

    return wrapper


@frame
def say_hello() -> None:
    print("Привет, игрок!")


say_hello()
