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
    # map проходит по продажам.
    # lambda считает выручку одного товара: количество * цена.
    revenue_pairs = map(lambda sale: (sale[0], sale[1] * sale[2]), sales)

    # sorted сортирует пары по выручке.
    # lambda берет выручку из одной пары.
    sorted_pairs = sorted(revenue_pairs, key=lambda pair: pair[1], reverse=True)

    # dict превращает пары в словарь.
    return dict(sorted_pairs)


result = calculate_sales(sales)
print(result)
print(str(result) == str(sample))