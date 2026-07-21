""" 03 Класс Teacher и список людей

На основе класса Person создайте класс Teacher.
- У преподавателя есть имя и предмет.
- Метод introduce() должен выводить имя и предмет.

Метод introduce() должен выводить строку:
    Hello, I am professor <имя>. My subject is <предмет>.

Создайте список, в котором будут Student и Teacher,
и вызовите у всех метод introduce().

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
Hello, I am professor Bob.
My subject is Mathematics
"""


# Источник: ../materials/theory_01__4_pillars_of_the_OOP.md — наследование и полиморфизм
# Источник: ../materials/theory_02__super.md — вызов конструктора родителя
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


class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def introduce(self) -> None:
        print(f"Hello, I am professor {self.name}.")
        print(f"My subject is {self.subject}")


student1 = Student("Alice", 2)
teacher1 = Teacher("Bob", "Mathematics")

people = [student1, teacher1]

for person in people:
    person.introduce()

# Hello, my name is Alice.
# I'm on course 2.
# Hello, I am professor Bob.
# My subject is Mathematics
