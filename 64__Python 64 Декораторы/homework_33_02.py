""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""

import time
from typing import Callable


# Источник: ../../python-course/40__Python 40 Модуль collections/materials/theory_01__time.md — time.time()
# Источник: ../../python-course/62__Python 62 Вложенные функции. Замыкание/materials/theory_02__Enclosing_scope.md — вложенные функции и замыкания
def measure_time(repeats: int = 5) -> Callable:
    """Вернуть декоратор с заданным количеством запусков функции."""

    def decorator(func: Callable[..., int]) -> Callable[..., int]:
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

    return decorator


@measure_time(10)
def compute() -> int:
    total = 0
    for number in range(10_000_000):
        total += number
    return total


print(f"Результат: {compute()}")
