""" 02 Фильтрация чисел по чётности

Напишите функцию filter_type, которая
- принимает первый аргумент ("even" или "odd")
- и произвольное количество чисел,
- возвращая только те, которые соответствуют фильтру.

Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""
# Проверяем, является ли число чётным.
def is_even(n):
    return n % 2 == 0


# Проверяем, является ли число нечётным.
def is_odd(n):
    return n % 2 != 0

# Функция для фильтрации чисел по чётности.
def filter_numbers(filter_type, *numbers):
    if filter_type == "even":
        result = []

        # Собираем только чётные числа.
        for number in numbers:
            if is_even(number):
                result.append(number)

        return result

    # Если выбран фильтр "odd", собираем только нечётные числа.
    if filter_type == "odd":
        result = []

        # Собираем только нечётные числа.
        for number in numbers:
            if is_odd(number):
                result.append(number)

        return result

    # Если фильтр не "even" и не "odd", возвращаем сообщение об ошибке.
    return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))   # [2, 4, 6]
print(filter_numbers("odd", 10, 15, 20, 25))      # [15, 25]
print(filter_numbers("prime", 2, 3, 5, 7))        # Некорректный фильтр
