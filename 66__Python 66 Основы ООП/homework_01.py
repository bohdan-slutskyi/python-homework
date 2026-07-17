"""01 Класс Rectangle

Создайте класс Rectangle, который описывает прямоугольник.
У каждого объекта должны быть два поля:
- width
- и height.
Добавьте метод get_area(), который возвращает площадь прямоугольника.
Создайте объект прямоугольника с произвольными значениями.
Выведите его площадь.
Измените ширину и высоту.
Выведите новую площадь.

Пример вывода:
Площадь: 20
Новая площадь: 35
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
