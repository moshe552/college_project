from managment_collection import ManagementCollection
from student import Student


class StudentManager(ManagementCollection):

    def __init__(self):
        super().__init__()

    def add(self, student: Student):
        super().add(student)

    def set_grade(self, student_id, course, grade):
        self.dict_of_items[student_id].grades[course] = grade

    def get_grade(self, student_id, course):
        return self.dict_of_items[student_id].grades[course]

    def average(self, student_id):
        student = self.dict_of_items[student_id]
        grades = student.grades
        grades_sum = sum(grades.values())
        num_of_courses = len(grades)
        return grades_sum // num_of_courses

