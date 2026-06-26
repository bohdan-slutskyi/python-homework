""" 03 Комбинации одежды

Напишите функцию, которая
- принимает списки
    - типов одежды,
    - цветов
    - и размеров,
- а затем генерирует все возможные комбинации в формате "Clothe - Color - Size".

Данные:
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L

"""

# источники:
# - materials/theory_04__itertools.md — itertools.product
# - materials/theory_05__generator_expression.py — генераторное выражение

from itertools import product
from typing import Generator


def get_product(
    clothes: list[str], colors: list[str], sizes: list[str]
) -> Generator[str, None, None]:
    """Генерирует все комбинации одежды, цвета и размера."""
    # product лениво строит все комбинации из трёх списков.
    # Генераторное выражение собирает строку для одной текущей комбинации.
    return (
        f"{cloth} - {color} - {size}"
        for cloth, color, size in product(clothes, colors, sizes)
    )


clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

for combination in get_product(clothes, colors, sizes):
    print(combination)
