from managment_collection import ManagementCollection
from student import Student


class StudentManager(ManagementCollection):

    def __init__(self):
        super().__init__()

    def add(self, student: Student):
        super().add(student)

    def set_grade(self, student_id: int, course_id: int, grade: int):
        if self.valid_item(student_id):
            student = self.get(student_id)
            if course_id in student.courses:
                self.dict_of_items[student_id].grades[course_id] = grade
            else:
                print("The student isn't participate in this course.")
        else:
            print("The student isn't exists.")

    def get_grade(self, student_id: int, course_id: int):
        if self.valid_item(student_id):
            student = self.get(student_id)
            if course_id in student.courses:
                return student.grades[course_id]
            return "The student isn't participate in this course."
        return "The student isn't exists."

    def grades_average(self, student_id: int):
        student = self.get(student_id)
        grades = student.grades
        grades_sum = sum(grades.values())
        num_of_courses = len(grades)
        return grades_sum // num_of_courses

