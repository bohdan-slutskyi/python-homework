"""01 Сортировка чисел

Напишите программу, которая
- запрашивает у пользователя три числа
- и выводит их в порядке возрастания, разделенные запятой.

ВАЖНО: при решении использовать ТОЛЬКО конструкцию if - elif - else
"""

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a <= b <= c:
    print(a, b, c, sep=", ")
elif a <= c <= b:
    print(a, c, b, sep=", ")
elif b <= a <= c:
    print(b, a, c, sep=", ")
elif b <= c <= a:
    print(b, c, a, sep=", ")
elif c <= a <= b:
    print(c, a, b, sep=", ")
else:
    print(c, b, a, sep=", ")

""" drugie varianty tut nizhe"""

# # Вариант 2
# if a <= b:
#     if b <= c:
#         print(a, b, c, sep=", ")
#     elif a <= c:
#         print(a, c, b, sep=", ")
#     else:
#         print(c, a, b, sep=", ")
# elif a <= c:
#     print(b, a, c, sep=", ")
# elif b <= c:
#     print(b, c, a, sep=", ")
# else:
#     print(c, b, a, sep=", ")

# Вариант 3
# if a <= b:
#     if a <= c:
#         if b <= c:
#             print(a, b, c, sep=", ")
#         else:
#             print(a, c, b, sep=", ")
#     else:
#         print(c, a, b, sep=", ")
# elif b <= c:
#     if a <= c:
#         print(b, a, c, sep=", ")
#     else:
#         print(b, c, a, sep=", ")
# else:
#     print(c, b, a, sep=", ")

# 4 вариант
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
# print(a, b, c, sep=", ")
