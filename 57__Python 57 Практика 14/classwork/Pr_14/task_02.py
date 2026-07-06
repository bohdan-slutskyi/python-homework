""" 02 Генератор случайных дат

Создайте генератор, который
- генерирует случайные даты в пределах одного года.

Генератор должен
- принимать год в качестве аргумента
- и выдавать следующую случайную дату при каждом вызове, учитывая
    - количество дней в месяце,
    - а также високосные годы.

Пример вывода:
2025-11-04
2025-01-24
2025-05-08
2025-04-05
2025-12-04
"""

import random
from datetime import date
random.seed(42)

def is_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# Генераторная функция: while True — бесконечная выдача случайных дат
def random_dates(year: int):
    days_in_month = [
        31, 29 if is_leap(year) else 28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]
    while True:
        month = random.randint(1, 12)
        day = random.randint(1, days_in_month[month - 1])
        yield date(year, month, day)  # при каждом yield возвращается одна дата


if __name__ == "__main__":
    gen = random_dates(2025)   # создаём объект-генератор

    # next() вручную запрашивает следующее значение у генератора
    for _ in range(5):
        print(next(gen))



