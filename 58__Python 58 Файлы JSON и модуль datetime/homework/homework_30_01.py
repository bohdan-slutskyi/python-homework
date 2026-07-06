"""01 Анализ курсов студентов

Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
    - Имя
    - дату рождения (birth_date) в формате дд.мм.гггг
    - дату поступления (enrollment_date) в том же формате
    - список курсов.

2. Вычислить:
    - общее количество студентов.
    - средний возраст на момент поступления.
    - количество студентов на каждом курсе.

3. Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from collections import Counter
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rld


def read_json(filename):
    # источник:
    # - materials/theory_01__JSON.md — json.load(), чтение JSON из файла
    # Открываем JSON-файл для чтения.
    with open(filename, "r", encoding="utf-8") as file:
        # json.load() превращает содержимое файла в Python-объект.
        return json.load(file)


def write_json(filename, data):
    # источник:
    # - materials/theory_01__JSON.md — json.dump(), indent, ensure_ascii=False
    # Открываем JSON-файл для записи результата.
    with open(filename, "w", encoding="utf-8") as file:
        # ensure_ascii=False сохраняет русские буквы нормально.
        # indent=4 делает файл читаемым.
        json.dump(data, file, indent=4, ensure_ascii=False)


def calculate_age(birth_date, enrollment_date):
    # источники:
    # - materials/theory_03__datetime.md — datetime.strptime(), строка -> datetime
    # - materials/theory_05__dateutil_relativedelta.md — relativedelta(...).years для возраста
    # Превращаем строки с датами в объекты datetime.
    birth = dt.strptime(birth_date, "%d.%m.%Y")
    enrollment = dt.strptime(enrollment_date, "%d.%m.%Y")

    # relativedelta считает разницу между датами в полных годах.
    return rld(enrollment, birth).years


def get_info():
    """
    "name": "Diana Williams",
    "birth_date": "12.06.1983",
    "enrollment_date": "29.04.2023",
    "courses": [
      "Physics",
      "Chemistry"
    ]
    """

    students = read_json("student_courses.json")

    total_students = len(students)
    ages = []
    all_courses = []

    for student in students:
        age = calculate_age(student["birth_date"], student["enrollment_date"])
        ages.append(age)
        all_courses.extend(student["courses"])

    average_age = round(sum(ages) / total_students, 2)

    # Counter удобно считает, сколько раз встречается каждый курс.
    # Здесь используем уже знакомую коллекцию Counter для подсчёта повторений.
    courses_count = dict(Counter(all_courses))

    # Формируем итоговый словарь для отчёта.
    # источник:
    # - materials/theory_02__JSON_vs_dict.md — Python dict как структура ключ-значение перед записью в JSON
    report = {
        "total_students": total_students,
        "average_age_at_enrollment": average_age,
        "students_per_course": courses_count
    }

    write_json("student_courses_report.json", report)
    print("Отчет успешно сохранен в student_courses_report.json")
    print(json.dumps(report, indent=4, ensure_ascii=False))


get_info()
