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

    while True:
        choice = int(input("""Welcome to Mivchar!
     1. Manage students
     2. Manage teachers
     3. Manage courses
     4. Exit program
     Please enter your choice:  """))
        if choice == 1:
            choice = int(input("""
         1. Add student
         2. Remove student
         3. Show student details
         4. Show all students
         5. Edit student details
         6. Student grades
         7. Show students courses
         8. Back to main menu
         9. Exit program
         Please enter your choice:  """))
            if choice == 1:
                print("Enter student details:")
                student_manager.add(Student(input("Please enter the student name: "),
                                            input("Please enter the student phone number: "),
                                            input("Please enter the student email: ")))
                continue
            if choice == 2:
                student_manager.remove(int(input("Please enter the student ID: ")))
                continue
            if choice == 3:
                print(student_manager.get(int(input("Enter the student ID: "))))
                continue
            if choice == 4:
                student_manager.print_items()
                continue
            if choice == 5:
                choice = int(input("""
                1. Edit student name
                2. Edit student phone
                3. Edit student email
                4. Back to main menu
                5. Exit program
                 Please enter your choice:  """))
                if choice == 1:
                    student = student_manager.get(int(input("Please enter the student ID: ")))
                    student.name = input("Please enter the new student name: ")
                    continue
                if choice == 2:
                    student = student_manager.get(int(input("Please enter the student ID: ")))
                    student.phone = input("Please enter the new student phone: ")
                    continue
                if choice == 3:
                    student = student_manager.get(int(input("Please enter the student ID: ")))
                    student.email = input("Please enter the new student email: ")
                    continue
                if choice == 4:
                    continue
                if choice == 5:
                    break
            if choice == 6:
                choice = int(input("""
                                1. Set student grade
                                2. Show student grade
                                3. Show student average grades
                                4. Back to main menu
                                5. Exit program
                                Please enter your choice:  """))
                if choice == 1:
                    student_manager.set_grade(int(input("Please enter the student ID: ")),
                                              int(input("Please enter the course ID: ")),
                                              int(input("Please enter the grade: ")))
                    continue
                if choice == 2:
                    print(student_manager.get_grade(int(input("Please enter the student ID: ")),
                                                    int(input("Please enter the course ID: "))))
                    continue
                if choice == 3:
                    print(student_manager.grades_average(int(input("Please enter the student ID: "))))
                    continue
                if choice == 4:
                    continue
                if choice == 5:
                    break
            if choice == 7:
                student_manager.show_person_courses(int(input("Please enter the student ID: ")))
                continue
            if choice == 8:
                continue
            if choice == 9:
                break

        if choice == 2:
            choice = int(input("""
                     1. Add teacher
                     2. Remove teacher
                     3. Show teacher details
                     4. Edit teacher details
                     5. Show teachers courses
                     6. Back to main menu
                     7. Exit program
                     Please enter your choice:  """))
            if choice == 1:
                teacher_manager.add(Teacher(input("Please enter the teacher name: "),
                                            input("Please enter the teacher phone number: "),
                                            input("Please enter the teacher email: "),
                                            input("Please enter the teacher salary: ")))
                continue
            if choice == 2:
                teacher_manager.remove(int(input("Please enter the teacher ID: ")))
                continue
            if choice == 3:
                print(student_manager.get(int(input("Enter the student ID: "))))
            if choice == 4:
                choice = int(input("""
                            1. Edit teacher name
                            2. Edit teacher phone
                            3. Edit teacher email
                            4. Edit teacher salary
                            5. Back to main menu
                            6. Exit program
                            Please enter your choice:  """))
                if choice == 1:
                    teacher = student_manager.get(int(input("Please enter the teacher ID: ")))
                    teacher.name = input("Please enter the new teacher name: ")
                    continue
                if choice == 2:
                    teacher = student_manager.get(int(input("Please enter the teacher ID: ")))
                    teacher.name = input("Please enter the new teacher phone: ")
                    continue
                if choice == 3:
                    teacher = student_manager.get(int(input("Please enter the teacher ID: ")))
                    teacher.name = input("Please enter the new teacher email: ")
                    continue
                if choice == 4:
                    teacher = student_manager.get(int(input("Please enter the teacher ID: ")))
                    teacher.name = int(input("Please enter the new teacher salary: "))
                    continue
                if choice == 5:
                    continue
                if choice == 6:
                    break
            if choice == 5:
                teacher_manager.show_person_courses(int(input("Please enter the teacher ID: ")))
                continue
            if choice == 6:
                continue
            if choice == 7:
                break
        if choice == 3:
            choice = int(input("""
                                 1. Add course
                                 2. Remove course
                                 3. Edit course name
                                 4. Show course details 
                                 5. Edit teacher
                                 6. Edit student
                                 7. Back to main menu
                                 8. Exit program
                                 Enter your choice:  """))
            if choice == 1:
                course_manager.add(Course(input("Please enter the course name: ")))
                continue
            if choice == 2:
                course_manager.remove(int(input("Please enter the course ID: ")))
                continue
            if choice == 3:
                course = course_manager.get(int(input("Please enter the course ID: ")))
                course.name = input("Enter the course name: ")
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
                    print(course_manager.get(int(input("Enter the course ID: "))))
                    continue
                if choice == 2:
                    course_manager.print_items()
                    continue
                if choice == 3:
                    teacher_id = course_manager.get(int(input("Enter the course ID: "))).teacher_id
                    print(teacher_manager.get(teacher_id))
                    continue
                if choice == 4:
                    course = course_manager.get(int(input("Enter the course ID: ")))
                    for student in course.students.values():
                        print(student)
                    continue
                if choice == 5:
                    print(course_manager.course_average_grades(int(input("Enter the course ID: "))))
                    continue
                if choice == 6:
                    continue
                if choice == 7:
                    break
            if choice == 5:
                choice = int(input("""   
                                        1. Add teacher
                                        2. Set teacher
                                        3. Back to main menu
                                        4. Exit program
                                        Enter your choice:  """))
                if choice == 1:
                    course_manager.add_teacher(int(input("Enter the course ID: ")),
                                               int(input("Enter the teacher ID: ")))
                    continue
                if choice == 2:
                    course_manager.set_teacher(int(input("Enter the course ID: ")),
                                               int(input("Enter the teacher ID: ")))
                    continue
                if choice == 3:
                    continue
                if choice == 4:
                    break
            if choice == 6:
                choice = int(input("""
                                          1. Add student
                                          2. Remove student
                                          3. Back to main menu
                                          4. Exit program
                                          Enter your choice:  """))
                if choice == 1:
                    course_manager.add_student(int(input("Enter the course ID: ")),
                                               int(input("Enter the student ID: ")))
                    continue
                if choice == 2:
                    course_manager.remove_student(int(input("Enter the course ID: ")),
                                                  int(input("Enter the student ID: ")))
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


main()
