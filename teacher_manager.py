from managment_collection import ManagementCollection
from teacher import Teacher


class TeacherManager(ManagementCollection):

    def __init__(self):
        super().__init__()

    def add(self, teacher: Teacher):
        super().add(teacher)

    def set_salary(self, teacher_id, new_salary):
        teacher = self.dict[teacher_id]
        teacher.salary = new_salary



