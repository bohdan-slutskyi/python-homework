""" 01 План по дням недели

Напишите программу, которая помогает планировать дела.
Программа должна
- бесконечно выводить план на следующий день недели,
- пока пользователь нажимает 'Enter'.

Данные:
# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
"""

# источники:
# - materials/theory_04__itertools.md — itertools.cycle
# - materials/theory_01_iterable_vs_iterator.py — next() и работа с iterator

from itertools import cycle

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"],
}

# cycle зацикливает дни недели, чтобы расписание не заканчивалось.
schedule_iterator = cycle(weekly_schedule.items())

while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")
    if user_input != "":
        break

    day, tasks = next(schedule_iterator)
    print(f"{day}: {', '.join(tasks)}")
