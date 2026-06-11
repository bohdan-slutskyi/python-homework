""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""

def sum_digits_non_tail(lst):
    # not lst значит, что список закончился.
    if not lst:
        return 0

    # lst[0] берёт первый элемент списка.
    first = lst[0]

    # lst[1:] берёт всё, кроме первого элемента.
    rest = lst[1:]

    # isinstance проверяет, является ли first вложенным списком.
    if isinstance(first, list):
        # Сначала считаем сумму внутри first, потом сумму rest.
        return sum_digits_non_tail(first) + sum_digits_non_tail(rest)

    # Если first — число, прибавляем его к сумме rest.
    return first + sum_digits_non_tail(rest)


def sum_digits_tail(lst, acc=0):
    # acc хранит сумму уже найденных чисел.
    # not lst значит, что список закончился.
    if not lst:
        return acc

    # lst[0] берёт первый элемент списка.
    first = lst[0]

    # lst[1:] берёт всё, кроме первого элемента.
    rest = lst[1:]

    # isinstance проверяет, является ли first вложенным списком.
    if isinstance(first, list):
        # first + rest разворачивает вложенный список в общий путь обхода.
        return sum_digits_tail(first + rest, acc)

    # Если first — число, добавляем его в acc и идём дальше.
    return sum_digits_tail(rest, acc + first)


nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_digits_tail(nested_numbers))      # 28
print(sum_digits_non_tail(nested_numbers))  # 28
