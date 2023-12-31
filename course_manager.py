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
        super().add_2_arguments(course, person_courses)

    def removing_course(self, course_id: int, person_courses: dict):
        super().remove_2_arguments(course_id, person_courses)

    def add_teacher(self, course_id: int, teacher_id: int):
        """
        Adding teacher to the course.
        :param course_id: The key of course instance.
        :param teacher_id: The id of the teacher.
        :return: None
        """
        course = self.get(course_id)
        course.teacher_id = teacher_id
        #  Adds the course instance to the teacher courses dictionary.
        teacher_courses = self.teacher_manager.get(teacher_id).courses
        self.adding_course(course, teacher_courses)

    def set_teacher(self, course_id: int, teacher_id: int):
        #  Removing the course instance from the old teacher courses dictionary.
        course = self.get(course_id)
        old_teacher_id = course.teacher_id
        teacher_courses = self.teacher_manager.dict_of_items[old_teacher_id].courses
        self.removing_course(course_id, teacher_courses)
        #  Adds the course instance to the new teacher courses dictionary.
        self.add_teacher(course_id, teacher_id)

    def add_student(self, course_id: int, student_id: int):
        """
        Adding a student instance to the course students dictionary,
        and the course to the student courses,
        and the course ID to the student grades.
        :param course_id: The key of the course instance.
        :param student_id: The variable(key) of the Student instance.
        :return: None
        """
        all_students = self.student_manager.dict_of_items
        student = all_students[student_id]
        course = self.get(course_id)
        course_students = course.students
        course_students[student.id] = student
        #  Adds the course instance to the student courses dictionary.
        self.adding_course(course, student.courses)
        #  Adds the course ID to the student grades
        self.student_manager.set_grade(student_id, course_id, 0)

    def remove_student(self, course_id: int, student_id: int):
        """
        Removing student instance from the course-students dictionary,
        and the course from his courses' dictionary, and the grade from his grades.
        :param course_id: The key of the course
        :param student_id: The key of the student
        :return: None
        """
        course = self.get(course_id)
        del course.students[student_id]
        #  Removing the course instance to the student courses dictionary.
        student_courses = self.student_manager.dict_of_items[student_id].courses
        self.removing_course(course_id, student_courses)
        #  Removing the course from student grades
        student = self.student_manager.get(student_id)
        del student.grades[course_id]

    def course_average_grades(self, course_id):
        course = self.get(course_id)
        students = course.students
        sum_grades = 0
        for student in students.values():
            for grade in student.grades.values():
                sum_grades += grade
        num_of_students = len(students)
        return sum_grades // num_of_students

