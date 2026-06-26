""" 03 Объединение списков продуктов

Напишите функцию, которая
- принимает несколько (много) списков с названиями продуктов
- и возвращает генератор, содержащий все продукты в нижнем регистре.

Выведите содержимое генератора.

Данные:
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

# источники:
# - materials/theory_04__itertools.md — itertools.chain
# - materials/theory_05__generator_expression.py — генераторное выражение

from itertools import chain
from typing import Generator

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def gen(*groups: list[str]) -> Generator[str, None, None]:
    """Возвращает генератор со всеми продуктами в нижнем регистре."""
    # chain проходит по нескольким спискам как по одной общей последовательности.
    # Генераторное выражение переводит текущее название в нижний регистр.
    return (product.lower() for product in chain(*groups))


for product in gen(fruits, vegetables, dairy):
    print(product)
