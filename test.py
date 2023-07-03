from college import College
from student import Student


mivchar = College('Mivchar')
mivchar.student_manager.add(Student('Moshe', '0543332221', 'Moshe@gmail.com'))
mivchar.student_manager.add(Student('Yosi', '0543332222', 'Yosi@gmail.com'))
mivchar.student_manager.set_grade(1, 'math', 100)
mivchar.student_manager.set_grade(1, 'science', 90)
mivchar.student_manager.set_grade(1, 'english', 80)
print(mivchar.student_manager.get_grade(1, 'english'))

print('hi')