""" 01 Среднее время выполнения

Создайте декоратор measure_time, который
- измеряет и выводит среднее время выполнения функции за 5 вызовов.

Функция может быть любой:
    например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000

"""

import time
from typing import Callable


# Источник: ../../python-course/40__Python 40 Модуль collections/materials/theory_01__time.md — time.time()
# Источник: ../../python-course/62__Python 62 Вложенные функции. Замыкание/materials/theory_02__Enclosing_scope.md — вложенные функции
def measure_time(func: Callable[..., int]) -> Callable[..., int]:
    """Выполнить функцию пять раз и вывести среднее время выполнения."""
    repeats = 5

    def wrapper(*args, **kwargs) -> int:
        start_time = time.time()

        for _ in range(repeats):
            result = func(*args, **kwargs)

        end_time = time.time()
        average_time = (end_time - start_time) / repeats
        print(
            f"Среднее время выполнения для {repeats} вызовов: "
            f"{average_time:.2f} секунд"
        )
        return result

    return wrapper


@measure_time
def compute() -> int:
    total = 0
    for number in range(10_000_000):
        total += number
    return total


print(f"Результат: {compute()}")
