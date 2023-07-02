from course_manager import CourseManager
from student_manager import StudentManager
from teacher_manager import TeacherManager


class College:

    def __init__(self, name):
        #  super().__init__()
        self.__name = name
        self.student_manager = StudentManager()
        self.teacher_manager = TeacherManager()
        self.course_manager = CourseManager(self.student_manager)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



