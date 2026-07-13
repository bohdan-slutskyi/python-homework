"""Извлечение дат
Реализуйте программу, которая должна:
Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Данные:
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."


Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022

"""
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

import re

# Источник: ../materials/theory_07__re_hierarchy.md — re.finditer() и Match.group()
# Источник: ../materials/repetition_python_60.md — обратная ссылка \1
date_pattern = r"\b\d{2}([./-])\d{2}\1\d{4}\b"

for date_match in re.finditer(date_pattern, text):
    # finditer возвращает полное совпадение, даже если в шаблоне есть группа.
    print(date_match.group())

# 15/03/2025
# 01.12.2024
# 09-09-2023
# 28/02/2022
