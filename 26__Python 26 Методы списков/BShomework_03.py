""" 3. Порядок чётных

Напишите программу, которая
- формирует новый список чисел.

Добавьте в него все элементы исходного списка, где:
- нечетные числа занимают те же позиции,
- чётные числа отсортированы между собой обратном порядке.

Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]
"""

numbers = [5, 2, 3, 8, 4, 1, 2, 7]

even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
even_numbers.sort()
result = []
# even_index = 0
# for num in numbers:
#     if num % 2 == 0:
#         result.append(even_numbers[even_index])
#         even_index += 1
#     else:
#         result.append(num)
# print("Список после сортировки:", result)
for num in numbers:
    if num % 2 == 0:
        result.append(even_numbers.pop())
    else:
        result.append(num)

print("Список после сортировки:", result)