""" 01 Сумма цифр числа

Напишите рекурсивную функцию, которая находит сумму всех цифр числа.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
num = 43197
Пример вывода:
24
"""

def sum_digits_non_tail(num):
    # num < 10 значит, что осталась одна последняя цифра.
    if num < 10:
        return num

    # num % 10 берёт последнюю цифру числа.
    last_digit = num % 10

    # num // 10 убирает последнюю цифру числа.
    remaining_digits = num // 10

    # Складываем последнюю цифру с суммой оставшихся цифр.
    return last_digit + sum_digits_non_tail(remaining_digits)


def sum_digits_tail(num, accumulator=0):
    # accumulator хранит сумму уже найденных цифр.
    # num < 10 значит, что осталась одна последняя цифра.
    if num < 10:
        return accumulator + num

    # num % 10 берёт последнюю цифру числа.
    last_digit = num % 10

    # num // 10 убирает последнюю цифру числа.
    remaining_digits = num // 10

    # Добавляем цифру в accumulator и идём дальше.
    return sum_digits_tail(remaining_digits, accumulator + last_digit)


print(sum_digits_non_tail(43197))  # 24
print(sum_digits_tail(43197))      # 24
