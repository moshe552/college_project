from managment_collection import ManagementCollection
from student_manager import StudentManager
#  from teacher_manager import TeacherManager


class CourseManager(ManagementCollection):

    def __init__(self, student_manager):
        super().__init__()
        if not isinstance(student_manager, StudentManager):
            raise Exception
        self.student_manager = student_manager
        # if not isinstance(student_manager, TeacherManager):
        #     raise Exception
        # self.teacher_manager = teacher_manager

    def set_teacher(self, course_id: int, new_teacher_id: int):
        """
        Replacing the course teacher.
        :param course_id: The key of course instance.
        :param new_teacher_id: The id of the teacher.
        :return: None
        """
        course = self.dict_of_things[course_id]
        course.teacher_id = new_teacher_id

    def get_students(self, course_id: int):
        """
        Gets the dictionary of students in the course that contains the instances of students.
        :param course_id: The key of the course instance.
        :return: Dictionary of the course students
        :type: dict
        """
        course = self.dict[course_id]
        return course.students

    def add_student(self, course_id: int, student_id: int):
        """
        Adding a student instance to the students-course dictionary using the get_student() method.
        :param course_id: The key of the course instance.
        :param student_id: The variable(key) of the Student instance.
        :return: None
        """
        all_students = self.student_manager.dict_of_things
        course = self.get_students(course_id)
        student = all_students[student_id]
        course[student.id] = student

    def remove_student(self, course_id: int, student_id: int):
        """
        Removing student instance from the course-students dictionary.
        :param course_id: The key of the course
        :param student_id: The key of the student
        :return: None
        """
        course = self.dict_of_things[course_id]
        del course.students[student_id]


