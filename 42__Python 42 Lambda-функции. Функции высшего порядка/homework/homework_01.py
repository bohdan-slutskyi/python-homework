""" 01 Выбор заказов

У вас есть список заказов.
Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
- Отбирает заказы дороже 500.
- Создаёт список названий отобранных продуктов в алфавитном порядке.
- Возвращает итоговый список названий.

Данные:
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

Пример вывода:
['Chair', 'Laptop']

"""
orders = [
    {"product": "Laptop", "price": 1200}, # Цена этого заказа больше 500, поэтому название продукта "Laptop" попадёт в итоговый список.
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800}, # Цена этого заказа больше 500, поэтому название продукта "Chair" попадёт в итоговый список.
    {"product": "Desk", "price": 400},
]

sample = ["Chair", "Laptop"] # Это ожидаемый результат, с которым мы сравниваем работу функции.

def select_expensive_orders(ords):
    # Filter запоминает правило: оставить только заказы дороже 500.
    # lambda проверяет, должен ли текущий заказ попасть в итоговый результат.
    expensive_orders = filter(lambda order: order["price"] > 500, ords)

    # Map получает только те заказы, которые filter оставил после отбора.
    # Lambda извлекает из каждого отобранного заказа название продукта.
    product_names = map(lambda order: order["product"], expensive_orders)
    # Результатом работы map будет объект, который будет выдавать названия дорогих продуктов.

    # sorted сортирует названия продуктов по алфавиту и возвращает готовый список.
    return sorted(product_names)

result = select_expensive_orders(orders)
print(result)
print(result == sample)
