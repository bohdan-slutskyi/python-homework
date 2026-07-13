"""2. Разделение списка тегов
Реализуйте программу, которая должна:
Прочитать строку с тегами, введёнными пользователем.
Разделить её на отдельные теги, независимо от того,
чем они были разделены (запятые, точки с запятой, слэши или пробелы).
Удалить лишние пробелы и пустые значения.

Данные:
tag_input = "python, data-science / machine-learning; AI  neural-networks"

Пример вывода:
['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']
"""
tag_input = "python, data-science / machine-learning; AI  neural-networks"

import re

# Источник: ../materials/theory_07__re_hierarchy.md — re.split()
separator_pattern = r"[,;/\s]+"
tags = [tag for tag in re.split(separator_pattern, tag_input) if tag]
print(tags)

# ['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']
