# --- exceptions.py ---
class TooManyStudentsError(Exception):
    def __init__(self, message="Група не може містити більше 10 студентів"):
        super().__init__(message)

# --- student.py ---
class Student:
    def __init__(self, gender, age, name, surname, record_book):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname
        self.record_book = record_book

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

# --- group.py ---
class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError()
        self.students.add(student)

    def delete_student(self, surname):
        self.students = {s for s in self.students if s.surname != surname}

    def find_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def __str__(self):
        return f'Group {self.name}:\n' + '\n'.join(str(s) for s in self.students)

# --- main code ---
if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')

    try:
        gr.add_student(st1)
        gr.add_student(st2)
        # Додаємо ще 9 студентів для перевірки винятку
        for i in range(9):
            gr.add_student(Student('Male', 20+i, f'Name{i}', f'Surname{i}', f'REG{i}'))

    except TooManyStudentsError as e:
        print(f'ПОМИЛКА: {e}')

    print(gr)

    assert gr.find_student('Jobs') == st1
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print("\nПісля видалення Taylor:")
    print(gr)
