"""Домашнее задание 32.1: фабрика функций округления."""

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
