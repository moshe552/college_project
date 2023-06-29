from college import College
from student import Student


mivchar = College('Mivchar')
mivchar.student_manager.add(Student('Moshe', '0543332221', 'Moshe@gmail.com'))
mivchar.student_manager.add(Student('Yosi', '0543332222', 'Yosi@gmail.com'))
mivchar.student_manager.print_all(1)

