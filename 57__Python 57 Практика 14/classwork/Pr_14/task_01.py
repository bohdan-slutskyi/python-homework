""" 01. Генератор, аналогичный range()

Создайте генератор custom_range(), который
- повторяет функциональность range(),
- принимая start, stop, step
- и возвращая последовательность чисел.

Данные:
custom_range(2, 10, 2)
Пример вывода:
2 4 6 8

Данные:
custom_range(10, 0, -3)
Пример вывода:
10 7 4 1
"""

# Генераторная функция: yield приостанавливает выполнение и возвращает значение
def custom_range(start: int, stop: int | None = None, step: int = 1):
    if step == 0:
        raise ValueError("step не может быть равен 0")

    if stop is None:
        start, stop = 0, start

    if step > 0:
        while start < stop:
            yield start        # следующее число при движении вперёд
            start += step
    elif step < 0:
        while start > stop:
            yield start        # следующее число при движении назад
            start += step


# for автоматически вызывает next() у генератора, пока не кончатся значения
for num in custom_range(2, 10, 2):
    print(num, end=" ")

# 2 4 6 8

print("\n==============================")

for num in custom_range(10, 0, -3):
    print(num, end=" ")

# 10 7 4 1