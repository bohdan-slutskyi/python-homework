"""01 Класс Rectangle.

Создайте класс Rectangle с полями width и height.
Метод get_area() возвращает площадь прямоугольника.
"""

# Источник: ../../python-course/66__Python 66 Основы ООП/materials/theory_01_OOP_4_principles.md — класс, атрибуты экземпляра и методы


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height


rect = Rectangle(4, 5)
print("Площадь:", rect.get_area())

rect.width = 7
rect.height = 5
print("Новая площадь:", rect.get_area())

# Площадь: 20
# Новая площадь: 35
