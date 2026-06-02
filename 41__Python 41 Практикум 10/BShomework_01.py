""" 01 Повторения букв

Реализуйте функцию, которая
- принимает текст
- и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.

Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""

from collections import Counter


def char_count(text):
    # Counter считает, сколько раз встречается каждый символ.
    # Текст привести к нижнему регистру
    # и оставить только буквы. Пробел и знак "!" считать не нужно.
    letters = []

    for char in text.lower():
        # isalpha() возвращает True только для букв.
        # Отсекаем пробелы, цифры и знаки препинания.
        if char.isalpha():
            letters.append(char)

    # Counter вернёт словарь-подобный объект:
    # ключ = буква, значение = сколько раз она встретилась.
    return Counter(letters)


text = "Programming is fun!"
sample = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}


print(char_count(text))
print(char_count(text) == sample)
