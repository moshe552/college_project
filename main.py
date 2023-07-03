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
    math_1 = Course('Math')
    course_manager.add(math_1)
    english_1 = Course('English')
    course_manager.add(english_1)
    comp_scie_1 = Course('Computer science')
    course_manager.add(comp_scie_1)
    comp_scie_2 = Course('Computer science')
    course_manager.add(comp_scie_2)

    #  creating Teachers instances
    barak = Teacher('Barak', '0546839475', 'barak@gmail.com', 85000)
    teacher_manager.add(barak)
    avi = Teacher('Avi', '0546839999', 'avi@gmail.com', 30000)
    teacher_manager.add(avi)
    elad = Teacher('Elad', '054685555', 'elad@gmail.com', 20000)
    teacher_manager.add(elad)

    #  adding teacher to the course
    course_manager.add_teacher(math_1.id, avi.id)
    course_manager.add_teacher(english_1.id, elad.id)
    course_manager.add_teacher(comp_scie_1.id, barak.id)
    course_manager.add_teacher(comp_scie_2.id, barak.id)

    #  shows the teacher courses:
    # print(barak.courses)
    # print(barak.courses[3])
    # for val in barak.courses.values():
    #     print(val.name)

    #  Replacing a teacher in a course:
    course_manager.set_teacher(english_1.id, barak.id)

    #  creating Students instances
    moshe = Student('Moshe', '0543332111', 'moshe@gmail.com')
    student_manager.add(moshe)
    yosi = Student('Yosi', '0543332222', 'yosi@gmail.com')
    student_manager.add(yosi)
    idan = Student('Idan', '0543332333', 'idan@gmail.com')
    student_manager.add(idan)
    aviv = Student('Aviv', '0543332444', 'aviv@gmail.com')
    student_manager.add(aviv)
    yakov = Student('Yakov', '0543332555', 'Yakov@gmail.com')
    student_manager.add(yakov)

    # Shows students details:
    # stu_dict = student_manager.dict_of_things
    # for val in stu_dict.values():
    #     print(val)

    # Removing a student from college:
    student_manager.remove(yosi.id)

    # #  Adds a student to a course:
    course_manager.add_student(math_1.id, moshe.id)
    course_manager.add_student(math_1.id, idan.id)
    course_manager.add_student(math_1.id, aviv.id)
    course_manager.add_student(english_1.id, moshe.id)
    course_manager.add_student(english_1.id, idan.id)
    course_manager.add_student(comp_scie_1.id, moshe.id)
    course_manager.add_student(comp_scie_2.id, idan.id)
    course_manager.add_student(comp_scie_2.id, yakov.id)

    #  Shows the course-students details:
    # math_students = course_manager.dict_of_items[math_1.id].students
    # counter = 1
    # for val in math_students.values():
    #     print("Math student num", counter, ": ", val)
    #     counter += 1
    # english_students = course_manager.dict_of_items[english_1.id].students
    # counter = 1
    # for val in english_students.values():
    #     print("English student num", counter, ": ", val)
    # comp_sien_1_students = course_manager.dict_of_items[comp_scie_1.id].students
    # counter = 1
    # for val in comp_sien_1_students.values():
    #     print("Computer science 1 student num", counter, ": ", val)
    # comp_sien_2_students = course_manager.dict_of_items[comp_scie_2.id].students
    # counter = 1
    # for val in comp_sien_2_students.values():
    #     print("Computer science 2 student num", counter, ": ", val)

    #  Removing a student from course:
    course_manager.remove_student(math_1.id, aviv.id)
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
