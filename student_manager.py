from managment_collection import ManagementCollection
from student import Student


class StudentManager(ManagementCollection):

    def __init__(self):
        super().__init__()

    def add(self, student: Student):
        super().add(student)

    def add_grade(self, student, grade):
        pass
