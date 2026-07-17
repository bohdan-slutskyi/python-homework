""" 02 Расширяемый логгер событий

Создайте функцию, которая
- возвращает функцию "вложенный логгер событий".

Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано)
и возвращать весь список событий.

Пример вызова:
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)

Пример вывода:
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29

"""

from datetime import datetime
from typing import Callable


# Источник: ../../python-course/62__Python 62 Вложенные функции. Замыкание/materials/theory_02__Enclosing_scope.md — сохранение состояния в замыкании
def make_logger() -> Callable:
    """Вернуть логгер, который хранит события между вызовами."""
    events: list[str] = []

    def logger(event: str = "") -> list[str]:
        if event:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{event}: {current_time}")

        # Список events остаётся доступен благодаря замыканию.
        return events

    return logger


log = make_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for saved_event in log():
    print(saved_event)
