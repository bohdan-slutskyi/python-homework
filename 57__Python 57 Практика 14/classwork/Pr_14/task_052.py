""" 5.2 Распределение задач

Функция task_assigner()
- читает файл tasks.txt
- и назначает задачи сотрудникам по очереди.

Она использует генератор для
- постепенного чтения новых задач
- и назначения этих задач сотрудникам.

Дополнительно: если файл tasks.txt отсутствует,
программа делает 5 попыток с паузой 3 секунды перед завершением:
Файл не найден, попытка 1/5...
Файл не найден, попытка 2/5...
Файл не найден, попытка 3/5...
Файл не найден, попытка 4/5...
Файл не найден, попытка 5/5...
Файл так и не найден. Завершаем работу.


Если же файл задач есть, то задачи распределяются между сотрудниками "по кругу":

Данные:
employees = ["Alice", "Bob", "Charlie"]

Пример вывода:
Alice выполняет: Подготовить отчёт
Bob выполняет: Провести собрание
Charlie выполняет: Проверить документацию
Alice выполняет: Разработать новый модуль
Bob выполняет: Настроить сервер
"""

import time
import itertools

# Генераторная функция: пытается открыть файл (до 5 попыток),
# затем читает строки и назначает их сотрудникам по кругу
def task_assigner(employees, filename="tasks.txt"):
    # for-else: break при успехе, else выполняется, если файл так и не открылся
    for attempt in range(1, 6):
        try:
            file = open(filename, "r", encoding="utf-8")
            break
        except FileNotFoundError:
            print(f"Файл не найден, попытка {attempt}/5...")
            if attempt < 5:
                time.sleep(3)   # пауза перед следующей попыткой
    else:
        print("Файл так и не найден. Завершаем работу.")
        return                  # return останавливает генератор (StopIteration)

    with file:
        # itertools.cycle бесконечно перебирает сотрудников по кругу
        employee_cycle = itertools.cycle(employees)
        while True:
            line = file.readline()   # читаем одну строку (или пустую, если данных нет)
            if line:
                task = line.strip()
                if task:
                    yield next(employee_cycle), task   # возвращаем (сотрудник, задача)
            else:
                time.sleep(3)   # новых задач пока нет — ждём и пробуем снова


if __name__ == "__main__":
    employees = ["Alice", "Bob", "Charlie"]
    task_generator = task_assigner(employees)

    # Генератор возвращает тюплы (сотрудник, задача) — распаковываем сразу в for
    for employee, task in task_generator:
        print(f"{employee} выполняет: {task}")

