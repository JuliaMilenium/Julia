class TooManyStudentsError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів."):
        self.message = message
        super().__init__(self.message)


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError()
        self.students.append(student)

    def __str__(self):
        return ", ".join(str(student) for student in self.students)


# --- Основна логіка ---
group = Group()

try:
    for i in range(11):  # 11 студентів — буде виняток
        student = Student(f"Студент {i+1}")
        group.add_student(student)
except TooManyStudentsError as e:
    print(f"Помилка: {e}")

print("Поточний склад групи:")
print(group)
