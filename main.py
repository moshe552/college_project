from college import College
from course import Course
from student import Student
from teacher import Teacher


def main():
    #  creating College instance named Mivchar
    mivchar = College('Mivchar')
    student_manager = mivchar.student_manager
    teacher_manager = mivchar.teacher_manager
    course_manager = mivchar.course_manager

    #  creating Courses instances
    course_manager.add(Course('Math'))
    course_manager.add(Course('English'))
    course_manager.add(Course('Computer science'))

    #  creating Teachers instances
    teacher_manager.add(Teacher('Barak', '0546839475', 'barak@gmail.com', 85000))
    teacher_manager.add(Teacher('Avi', '0546839999', 'avi@gmail.com', 30000))
    teacher_manager.add(Teacher('Elad', '054685555', 'elad@gmail.com', 20000))

    #  adding teacher to the course
    course_manager.add_teacher(1, 2)
    course_manager.add_teacher(2, 3)
    course_manager.add_teacher(3, 1)

    #  shows the teacher courses:

    #
    # #  creating Students instances
    # student_manager.add(Student('Moshe', '0543332111', 'moshe@gmail.com'))
    # student_manager.add(Student('Yosi', '0543332222', 'yosi@gmail.com'))
    # student_manager.add(Student('Idan', '0543332333', 'idan@gmail.com'))
    # student_manager.add(Student('Aviv', '0543332444', 'aviv@gmail.com'))
    # student_manager.add(Student('Yakov', '0543332555', 'Yakov@gmail.com'))
    #
    # #  Adds a student to a course:
    # course_manager.add_student(1, 4)
    # course_manager.add_student(1, 5)
    # course_manager.add_student(1, 7)
    # course_manager.add_student(2, 4)
    # course_manager.add_student(2, 6)
    # course_manager.add_student(3, 4)
    # course_manager.add_student(3, 5)
    # course_manager.add_student(3, 8)
    #
    # #  Gets the course-students dictionary:
    # course_manager.get_students(1)
    # course_manager.get_students(2)
    # course_manager.get_students(3)
    #
    # #  Removing a student from course:
    # course_manager.remove_student(1, 7)
    #
    # #  replacing the teacher in the course:
    # course_manager.set_teacher(2, 1)
    # print(course_manager.dict_of_things[2].teacher_id)
    #
    # #  Adds grades to Moshe that is ID is "4"
    # student_manager.set_grade(4, 'Math', 100)
    # student_manager.set_grade(4, 'Computer science', 90)
    # student_manager.set_grade(4, 'English', 80)
    #
    # #  Adds grades to Idan that is ID is "6"
    # student_manager.set_grade(6, 'Math', 100)
    # student_manager.set_grade(6, 'Computer science', 95)
    # student_manager.set_grade(6, 'English', 100)
    #
    # #  get student
    # moshe = student_manager.get(4)
    # print(moshe)
    #
    # #  grades of students
    # print(student_manager.get_grade(4, "Math"))
    # print(student_manager.average(4))


main()
