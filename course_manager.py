from course import Course
from managment_collection import ManagementCollection
from student_manager import StudentManager
from teacher_manager import TeacherManager


class CourseManager(ManagementCollection):

    def __init__(self, student_manager, teacher_manager):
        super().__init__()
        if not isinstance(student_manager, StudentManager):
            raise Exception
        self.student_manager = student_manager
        if not isinstance(teacher_manager, TeacherManager):
            raise Exception
        self.teacher_manager = teacher_manager

    def add(self, course: Course):
        super().add(course)

    def adding_course(self, course: Course, person_courses: dict):
        super().adding(course, person_courses)

    def removing_course(self, course_id: int, person_courses: dict):
        super().removing(course_id, person_courses)

    def add_teacher(self, course_id: int, teacher_id: int):
        """
        לדעתי ניתן לאחד את הפונקצייה הזאת שתשמש גם את סטודנט וגם את המרצה,
         יתכן וניתן אף לאחד את הקלאסים לperson_manager
        Adding teacher to the course.
        :param course_id: The key of course instance.
        :param teacher_id: The id of the teacher.
        :return: None
        """
        course = self.dict_of_items[course_id]
        course.teacher_id = teacher_id
        #  Adds the course instance to the teacher courses dictionary.
        teacher_courses = self.teacher_manager.dict_of_items[teacher_id].courses
        self.adding_course(course, teacher_courses)

    def set_teacher(self, course_id: int, teacher_id: int):
        #  Removing the course instance from the old teacher courses dictionary.
        course = self.get(course_id)
        old_teacher_id = course.teacher_id
        teacher_courses = self.teacher_manager.dict_of_items[old_teacher_id].courses
        self.removing_course(course_id, teacher_courses)
        #  Adds the course instance to the new teacher courses dictionary.
        self.add_teacher(course_id, teacher_id)

    def get_course_items(self, course_id: int, items):
        """
        Gets the dictionary of items in the course that contains the instances of items.
        :param course_id: The key of the course instance.
        :return: Dictionary of the course items
        :type: dict
        """
        course = self.get(course_id)
        return course.items

    def add_student(self, course_id: int, student_id: int):
        """
        Adding a student instance to the students-course dictionary using the get_student() method.
        :param course_id: The key of the course instance.
        :param student_id: The variable(key) of the Student instance.
        :return: None
        """
        all_students = self.student_manager.dict_of_items
        student = all_students[student_id]
        course_students = self.get_students(course_id)
        course_students[student.id] = student
        #  Adds the course instance to the student courses dictionary.
        course = self.dict_of_items[course_id]
        self.adding_course(course, student.courses)

    def remove_student(self, course_id: int, student_id: int):
        """
        Removing student instance from the course-students dictionary,
        and the course from his courses' dictionary.
        :param course_id: The key of the course
        :param student_id: The key of the student
        :return: None
        """
        course = self.get(course_id)
        del course.students[student_id]
        #  Removing the course instance to the student courses dictionary.
        student_courses = self.student_manager.dict_of_items[student_id].courses
        self.removing_course(course_id, student_courses)

    def average(self, course_id):
        course = self.dict_of_items[course_id]
        grades = course.student.grades
        grades_sum = sum(grades.values())
        num_of_students = len(grades)
        return grades_sum // num_of_students

