"""02 Группировка студентов по классам

Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.

Данные:
students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy")
]

Пример вывода:
{
    'class1': ['Alice', 'Charlie'],
    'class2': ['Bob'],
    'class3': ['Daisy']
}
"""

from collections import defaultdict


def get_students_groups(students):
    # defaultdict(list) создаёт словарь.
    # Для нового класса сразу даёт пустой список.
    groups = defaultdict(list)

    for class_name, student_name in students:
        # class_name — ключ словаря.
        # student_name добавляем в список этого класса.
        groups[class_name].append(student_name)

    # Возвращаем обычный словарь для сравнения с sample.
    return dict(groups)

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
sample = {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}


print(get_students_groups(students))
print(get_students_groups(students) == sample)
