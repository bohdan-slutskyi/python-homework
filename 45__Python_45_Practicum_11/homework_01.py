"""01 Объединение данных в строку

Напишите функцию, которая
- принимает список любых данных (строки, числа, списки, словари)
- и возвращает их строковое представление, объединённое через " | ".
  (т.е. объединяет результат в одну строку)

Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.


Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
Пример вывода:
42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
"""


def join_data_loop(data: list[object]) -> str:
    """Способ 1: собирает строковые части через обычный цикл."""

    parts = []

    for item in data:
        # str(item) превращает один текущий элемент в строку
        parts.append(str(item))

    return " | ".join(parts)


def join_data_comprehension(data: list[object]) -> str:
    """Способ 2: собирает строковые части через comprehension."""

    # comprehension проходит по всему списку data
    # str(item) превращает один текущий элемент в строку
    parts = [str(item) for item in data]

    return " | ".join(parts)


data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

print(join_data_loop(data))
print(join_data_comprehension(data))
