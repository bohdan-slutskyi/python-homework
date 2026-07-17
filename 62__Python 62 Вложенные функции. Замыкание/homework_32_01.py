""" 01 Фабрика функций округления

Создайте функцию make_rounder(), которая
 - принимает количество знаков для округления
 - и возвращает другую функцию.

Полученная функция должна принимать число и возвращать его,
округлённое до указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

Пример вывода:
3.14
2.72
10.0
"""

from typing import Callable


# Источник: ../../python-course/62__Python 62 Вложенные функции. Замыкание/materials/theory_02__Enclosing_scope.md — вложенные функции и замыкания
def make_rounder(num_digits: int) -> Callable[[float], float]:
    """Вернуть функцию, округляющую числа до заданного количества знаков."""

    def round_number(number: float) -> float:
        # Вложенная функция запоминает num_digits из внешней функции.
        return round(number, num_digits)

    return round_number


round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))
