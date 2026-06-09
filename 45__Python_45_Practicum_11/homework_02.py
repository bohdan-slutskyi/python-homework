"""02 Сумма вложенных чисел

Напишите функцию, которая
- принимает список словарей, где каждый словарь содержит
    - имя пользователя
    - и список баллов.
- Функция должна вернуть сумму всех чисел.
- Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.

Данные:
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

Пример вывода:
Итоговый балл: 156
"""


def sum_nested_scores_loop(data: list[dict[str, list[int]]]) -> int:
    """Способ 1: считает сумму баллов через обычный цикл."""

    total = 0

    for user in data:
        # user["scores"] берёт список баллов одного пользователя
        scores = user["scores"]
        total += sum(scores)

    return total


def sum_nested_scores_comprehension(data: list[dict[str, list[int]]]) -> int:
    """Способ 2: считает сумму баллов через comprehension."""

    # comprehension проходит по всем пользователям в data
    # sum(user["scores"]) считает сумму баллов одного пользователя
    user_totals = [sum(user["scores"]) for user in data]

    return sum(user_totals)


data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]},
]

print("Способ 1:", "Итоговый балл:", sum_nested_scores_loop(data))
print("Способ 2:", "Итоговый балл:", sum_nested_scores_comprehension(data))
