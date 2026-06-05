""" 02 Статистика продаж

Дан двумерный массив продаж (список тюплов): (товар, количество, цена).

Напишите программу, которая:
- Вычисляет общую выручку для каждого товара.
- Возвращает словарь с товарами {товар: выручка},
    отсортированный по убыванию выручки.

Данные:
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800),
]

Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

"""

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800),
]

sample = {"Chair": 16000, "Laptop": 6000, "Monitor": 3000, "Keyboard": 1500, "Mouse": 1000}


def calculate_sales(sales):
    # sale - это один элемент из списка sales, то есть кортеж (товар, количество, цена).
    # map запоминает правило: для каждого товара sale[0] посчитать выручку (количество * цена = sale[1] * sale[2]).
    # lambda создаёт пару: название товара и его выручка.
    revenue_pairs = map(lambda sale: (sale[0], sale[1] * sale[2]), sales)

    # pair - это одна пара (товар, выручка) из revenue_pairs.
    # sorted сортирует товары по выручке от большей к меньшей.
    # lambda показывает sorted, что сортировать нужно по выручке pair[1]. 
    # reverse=True говорит, что сортировать нужно в обратном порядке, то есть от большей выручки к меньшей.
    sorted_pairs = sorted(revenue_pairs, key=lambda pair: pair[1], reverse=True)

    # dict собирает отсортированные пары в итоговый словарь.
    return dict(sorted_pairs)


result = calculate_sales(sales)
print(result)
print(str(result) == str(sample))