""" 01. Одно слово

Напишите программу, которая
- обрабатывает список из строк
- и удаляет все строки, содержащие более одного слова,
- а также преобразует оставшиеся строки к нижнему регистру.

ВАЖНО: НЕ создать новый список, а УДАЛИТЬ лишние элементы из существующего!

Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# print(text_list)
# for i in range(len(text_list) - 1, -1, -1):
#     if len(text_list[i].split()) > 1:
#         del text_list[i]
#     else:
#         text_list[i] = text_list[i].lower()
# print(f"Обработанный список: {text_list}")
"""вариант 2 - удаление элементов по индексу справа налево"""
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
print("Исходный список:", text_list)  # для наглядности, чтобы показать, что мы работаем с тем же списком
# проходим по списку в обратном порядке, чтобы избежать проблем с изменением индексов при удалении элементов
for i in reversed(range(len(text_list))):
    # если в строке есть пробел, значит строка содержит больше одного слова
    if " " in text_list[i]:
        # удаляем элемент по индексу из существующего списка
        del text_list[i]
    else:
        # если строка состоит из одного слова, заменяем её на нижний регистр
        text_list[i] = text_list[i].lower()

print("Обработанный список:", text_list)
