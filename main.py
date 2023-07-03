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

    # #  creating Courses instances
    # math_1 = Course('Math')
    # course_manager.add(math_1)
    # english_1 = Course('English')
    # course_manager.add(english_1)
    # comp_scie_1 = Course('Computer science')
    # course_manager.add(comp_scie_1)
    # comp_scie_2 = Course('Computer science')
    # course_manager.add(comp_scie_2)
    #
    # #  creating Teachers instances
    # barak = Teacher('Barak', '0546839475', 'barak@gmail.com', 85000)
    # teacher_manager.add(barak)
    # avi = Teacher('Avi', '0546839999', 'avi@gmail.com', 30000)
    # teacher_manager.add(avi)
    # elad = Teacher('Elad', '054685555', 'elad@gmail.com', 20000)
    # teacher_manager.add(elad)

    while True:
        choice = int(input("""Welcome to Mivchar!
         1. manage students
         2. manage teachers
         3. manage courses
         4. Exit program
         Please enter your choice:  """))
        if choice == 1:
            choice = int(input("""
         1. add student
         2. remove student
         3. Show student details
         4. edit student details
         5. student grades
         6. Show students courses
         7. Back to main menu
         8. Exit program
         Please enter your choice:  """))
            if choice == 1:
                print("Enter student details:")
                name = input("Please enter the student name: ")
                phone = input("Please enter the student phone number: ")
                email = input("Please enter the student email: ")
                student_manager.add(Student(name, phone, email))
                continue
            if choice == 2:
                student_manager.remove(int(input("Please enter the student ID: ")))
                continue
            if choice == 3:
                print(student_manager.get(int(input("Enter the student ID: "))))
            if choice == 4:
                choice = int(input("""
                1. Edit student name
                2. Edit student phone
                3. Edit student email
                4. Back to main menu
                5. Exit program
                 Please enter your choice:  """))
                if choice == 1:
                    pass
                    continue
                if choice == 2:
                    pass
                    continue
                if choice == 3:
                    pass
                    continue
                if choice == 4:
                    continue
                if choice == 5:
                    break
            if choice == 5:
                choice = int(input("""
                                1. Set student grade
                                2. Show student grades
                                3. Show student average grades
                                4. Back to main menu
                                5. Exit program
                                Please enter your choice:  """))
                if choice == 1:
                    pass
                    continue
                if choice == 2:
                    pass
                    continue
                if choice == 3:
                    pass
                    continue
                if choice == 4:
                    continue
                if choice == 5:
                    break
            if choice == 6:
                pass
                continue
            if choice == 7:
                pass
                continue
            if choice == 8:
                continue
            if choice == 9:
                break
        if choice == 2:
            choice = int(input("""
                     1. add teacher
                     2. remove teacher
                     3. Show teacher details
                     4. edit teacher details
                     5. Show teachers courses
                     6. Back to main menu
                     7. Exit program
                     Please enter your choice:  """))
            if choice == 1:
                pass
                continue
            if choice == 2:
                pass
                continue
            if choice == 3:
                print(student_manager.get(int(input("Enter the student ID: "))))
            if choice == 4:
                choice = int(input("""
                            1. Edit student name
                            2. Edit student phone
                            3. Edit student email
                            Please enter your choice:  """))
            if choice == 5:
                pass
                continue
            if choice == 6:
                continue
            if choice == 7:
                break
        if choice == 3:
            choice = int(input("""
                                 1. add course
                                 2. remove course
                                 3. Set course name 
                                 4. Show course details
                                 5. Edit teacher
                                 6. Edit student
                                 7. Back to main menu
                                 8. Exit program
                                 Enter your choice:  """))
            if choice == 1:
                pass
                continue
            if choice == 2:
                pass
                continue
            if choice == 3:
                pass
                continue
            if choice == 4:
                choice = int(input("""
                          1. Show course details
                          2. Show courses
                          3. Show course teacher
                          4. Show course students
                          5. Show course average grades
                          6. Back to main menu
                          7. Exit program
                          Enter your choice:  """))
                if choice == 1:
                    pass
                    continue
                if choice == 2:
                    pass
                    continue
                if choice == 3:
                    pass
                    continue
                if choice == 4:
                    pass
                    continue
                if choice == 5:
                    pass
                    continue
                if choice == 6:
                    continue
                if choice == 7:
                    break
            if choice == 5:
                choice = int(input("""    1. Add teacher
                                          2. Set teacher
                                          3. Back to main menu
                                          4. Exit program
                                          Enter your choice:  """))
                if choice == 1:
                    pass
                    continue
                if choice == 2:
                    pass
                    continue
                if choice == 3:
                    continue
                if choice == 4:
                    break
            if choice == 6:
                choice = int(input("""
                                          1. Add student
                                          2. Set student
                                          3. Back to main menu
                                          4. Exit program
                                          Enter your choice:  """))
                if choice == 1:
                    pass
                    continue
                if choice == 2:
                    pass
                    continue
                if choice == 3:
                    continue
                if choice == 4:
                    break
            if choice == 7:
                continue
            if choice == 8:
                break
        if choice == 4:
            break



    #
    #
    # #  adding teacher to the course
    # course_manager.add_teacher(math_1.id, avi.id)
    # course_manager.add_teacher(english_1.id, elad.id)
    # course_manager.add_teacher(comp_scie_1.id, barak.id)
    # course_manager.add_teacher(comp_scie_2.id, barak.id)
    #
    # #  shows the teacher courses:
    # # print(barak.courses)
    # # print(barak.courses[3])
    # # for val in barak.courses.values():
    # #     print(val.name)
    #
    # #  Replacing a teacher in a course:
    # course_manager.set_teacher(english_1.id, barak.id)
    #
    # #  creating Students instances
    # moshe = Student('Moshe', '0543332111', 'moshe@gmail.com')
    # student_manager.add(moshe)
    # yosi = Student('Yosi', '0543332222', 'yosi@gmail.com')
    # student_manager.add(yosi)
    # idan = Student('Idan', '0543332333', 'idan@gmail.com')
    # student_manager.add(idan)
    # aviv = Student('Aviv', '0543332444', 'aviv@gmail.com')
    # student_manager.add(aviv)
    # yakov = Student('Yakov', '0543332555', 'Yakov@gmail.com')
    # student_manager.add(yakov)
    #
    # # Shows students details:
    # # stu_dict = student_manager.dict_of_things
    # # for val in stu_dict.values():
    # #     print(val)
    #
    # # Removing a student from college:
    # student_manager.remove(yosi.id)
    #
    # # #  Adds a student to a course:
    # course_manager.add_student(math_1.id, moshe.id)
    # course_manager.add_student(math_1.id, idan.id)
    # course_manager.add_student(math_1.id, aviv.id)
    # course_manager.add_student(english_1.id, moshe.id)
    # course_manager.add_student(english_1.id, idan.id)
    # course_manager.add_student(comp_scie_1.id, moshe.id)
    # course_manager.add_student(comp_scie_2.id, idan.id)
    # course_manager.add_student(comp_scie_2.id, yakov.id)

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
    # course_manager.remove_student(math_1.id, aviv.id)
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
