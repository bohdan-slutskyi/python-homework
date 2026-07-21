""" 01 Класс Person

Создайте класс Person, представляющий человека.
- Каждый человек должен иметь имя.
- Добавьте метод introduce(), который выводит приветствие с именем.

Пример вывода:
Hello, my name is Alice.
"""


# Источник: ../materials/theory_01__4_pillars_of_the_OOP.md — класс и метод объекта
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        print(f"Hello, my name is {self.name}.")


person1 = Person("Alice")
person1.introduce()

# Hello, my name is Alice.
