"""Домашнее задание 32.2: расширяемый логгер событий."""

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
