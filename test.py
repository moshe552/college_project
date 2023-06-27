from college import College
from student import Student


mivchar = College('Mivchar')
moshe = Student('Moshe', '0543332221', 'Moshe@gmail.com', mivchar.students)
yosi = Student('Yosi', '0543332222', 'Yosi@gmail.com', mivchar.students)
print(mivchar.students)
