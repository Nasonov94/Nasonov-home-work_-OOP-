class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finish_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, courses_name):
        self.finish_courses.append(courses_name)

    def grade_hw(self, lecturer, course, grate):
        if (
            isinstance(lecturer, Lecturer)
            and self.courses_in_progress
            and course in lecturer.courses_attached
            and (10 >= grate >= 0)
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grate]
            else:
                lecturer.grades[course] = [grate]

        else:
            return "Ошибка"

    def average_value(self):
        sum_grades = 0
        total_grades = 0

        for i in self.grades.values():
            sum_grades += sum(i)
            total_grades += len(i)
        return sum_grades / total_grades

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_value()}\n"
            f"Курсы в процесе изучения: {self.courses_in_progress}\n"
            f"Завершенные курсы {self.finish_courses}"
        )

    def __gt__(self, other):
        return self.average_value() > other.average_value()

    @staticmethod
    def all_average_course(student_list, course_name):
        total_sum = 0
        total_count = 0

        for student in student_list:
            if course_name in student.grades:
                total_sum += sum(student.grades[course_name])
                total_count += len(student.grades[course_name])

        if total_count > 0:
            return total_sum / total_count
        return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_value(self):
        sum_grades = 0
        total_grades = 0

        for i in self.grades.values():
            sum_grades += sum(i)
            total_grades += len(i)
        return sum_grades / total_grades

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}\n Средняя оценка за лекции: {self.average_value()}"

    def __gt__(self, other):
        return self.average_value() > other.average_value()

    @staticmethod
    def all_average_course(lecturer_list, course_name):
        total_sum = 0
        total_count = 0

        for lecturer in lecturer_list:
            if course_name in lecturer.grades:
                total_sum += sum(lecturer.grades[course_name])
                total_count += len(lecturer.grades[course_name])

        if total_count > 0:
            return total_sum / total_count
        return 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def grate_hw(self, student, course, grate):
        if (
            isinstance(student, Student)
            and self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grate]
            else:
                student.grades[course] = [grate]
        else:
            return "Ошибка"


# lecturer = Lecturer("Иван", "Иванов")
# reviewer = Reviewer("Пётр", "Петров")
# print(isinstance(lecturer, Mentor))
# print(isinstance(reviewer, Mentor))
# print(lecturer.courses_attached)
# print(reviewer.courses_attached)

student_1 = Student("Ivan", "Petrov")
student_1.courses_in_progress = ["Python", "JavaScript"]

student_2 = Student("Denis", "Ivanov")
student_2.courses_in_progress = ["JavaScript", "Python"]

reviewer_1 = Reviewer("Anton", "Demidov")
reviewer_1.courses_attached = ["Python"]

reviewer_2 = Reviewer("Petro", "Demidoviv")
reviewer_2.courses_attached = ["JavaScript"]


lektrer_1 = Lecturer("Taras", "Labuda")
lektrer_1.courses_attached = ["Python", "JavaScript"]

lektrer_2 = Lecturer("Oleg", "Vasilev")
lektrer_2.courses_attached = ["JavaScript", "Python"]

student_1.grade_hw(lektrer_1, "Python", 5)
student_1.grade_hw(lektrer_1, "Python", 10)
student_1.grade_hw(lektrer_1, "Python", 2)
student_1.grade_hw(lektrer_1, "Python", 7)

student_2.grade_hw(lektrer_2, "JavaScript", 7)
student_2.grade_hw(lektrer_2, "JavaScript", 7)


reviewer_1.grate_hw(student_1, "Python", 8)
reviewer_1.grate_hw(student_1, "Python", 2)
reviewer_1.grate_hw(student_1, "Python", 8)

reviewer_1.grate_hw(student_2, "Python", 2)
reviewer_1.grate_hw(student_2, "Python", 4)
reviewer_1.grate_hw(student_2, "Python", 6)

reviewer_2.grate_hw(student_2, "JavaScript", 2)
reviewer_2.grate_hw(student_2, "JavaScript", 8)
reviewer_2.grate_hw(student_2, "JavaScript", 10)


reviewer_2.grate_hw(student_1, "JavaScript", 4)
reviewer_2.grate_hw(student_1, "JavaScript", 4)
reviewer_2.grate_hw(student_1, "JavaScript", 7)

all_student = [student_1, student_2]

avg = Student.all_average_course(all_student, "Python")
print(avg)
