""" 04 Генератор тестовых данных

Создайте генератор, который
- принимает в качестве аргументов другие генераторы;
- и возвращает тюплы, состоящие из значений, полученных от каждого из них.

Используйте ранее написанные генераторы дат и имён для создания тестовых данных.

Данные:
name_gen = random_names()
date_gen = random_dates(2025)

Пример вывода:
('Emma Brown', '2025-02-14')
('Bob Williams', '2025-06-28')
('Charlie Johnson', '2025-09-09')
...
"""
from task_02 import random_dates
from task_03 import random_names

# Генератор: принимает несколько генераторов и собирает их значения в тюпл
def combine_generators(*generators):
    while True:
        # next() берёт по одному значению из каждого генератора
        yield tuple(next(g) for g in generators)


if __name__ == "__main__":
    # Создаём объекты-генераторы
    name_gen = random_names()
    date_gen = random_dates(2025)

    # Передаём их как аргументы в комбинирующий генератор
    data_gen = combine_generators(name_gen, date_gen)

    # next(data_gen) возвращает тюпл вида (имя, дата)
    for _ in range(5):
        print(next(data_gen))
