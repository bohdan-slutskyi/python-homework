""" 02 Класс Student

На основе класса Person создайте класс Student.
- Студент должен иметь имя и номер курса.
- Метод introduce() должен
    - сначала выводить базовое приветствие,
    - а затем строку: I'm on course <номер_курса>.

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
"""


# Источник: ../materials/theory_02__super.md — наследование и super()
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name: str, course_number: int) -> None:
        super().__init__(name)
        self.course_number = course_number

    def introduce(self) -> None:
        super().introduce()
        print(f"I'm on course {self.course_number}.")


student1 = Student("Alice", 2)
student1.introduce()

# Hello, my name is Alice.
# I'm on course 2.
