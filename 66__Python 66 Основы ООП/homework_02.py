"""02 Класс Counter.

Счётчик начинается с нуля, изменяется методами increase() и decrease()
и возвращает текущее значение через get_value().
"""

# Источник: ../../python-course/66__Python 66 Основы ООП/materials/theory_01_OOP_4_principles.md — класс, атрибут экземпляра и методы


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increase(self) -> None:
        self.value += 1
        print(f"Значение увеличено, текущее: {self.value}")

    def decrease(self) -> None:
        self.value -= 1
        print(f"Значение уменьшено, текущее: {self.value}")

    def get_value(self) -> int:
        return self.value


counter = Counter()
counter.increase()
counter.increase()
counter.increase()
counter.decrease()
print(f"Текущее значение: {counter.get_value()}")

# Значение увеличено, текущее: 1
# Значение увеличено, текущее: 2
# Значение увеличено, текущее: 3
# Значение уменьшено, текущее: 2
# Текущее значение: 2
