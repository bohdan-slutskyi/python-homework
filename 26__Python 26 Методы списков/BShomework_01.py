""" 01 Число в конце

Напишите программу, которая
- создает новый список.
В него необходимо добавить только те строки из исходного списка,
в которых цифры находятся только в конце.

Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
"""
#strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# result = []
#
# for string in strings:
#     digit_index = -1
#
#     for index in range(len(string)):
#         if string[index].isdigit():
#             digit_index = index
#             break
#
#     if digit_index != -1:
#         letters = string[:digit_index]
#         digits = string[digit_index:]
#
#         if letters.isalpha() and digits.isdigit():
#             result.append(string)
#
# print("Строки с цифрами только в конце:", result)
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
result = []
for word in strings:
    if word.rstrip('0123456789').isalpha(): # 
        result.append(word) #
print("Строки с цифрами только в конце:", result)

