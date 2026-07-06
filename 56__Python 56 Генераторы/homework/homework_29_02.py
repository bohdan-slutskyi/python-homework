""" 02 Генератор уникальных элементов

Создайте генератор, который
- принимает список элементов и выдаёт только уникальные значения,
сохраняя порядок их появления в исходном списке

Входные данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

Пример вывода:
3
1
2
4
5
6
7
8

"""
from typing import Generator, Any


def generator_unique(items: list[Any]) -> Generator[Any, None, None]:
    # источники:
    # - materials/theory_02__generator_function.md — генераторная функция и yield
    # - materials/theory_01__Generator_vs_Iterator.md — генератор выдаёт значения по одному
    # Создаём список для уже встреченных элементов.
    seen = []

    for item in items:
        # Если такого элемента ещё не было, выдаём его.
        if item not in seen:
            seen.append(item)
            yield item

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


for x in generator_unique(data):
    print(x)

# 3
# 1
# 2
# 4
# 5
# 6
# 7
# 8