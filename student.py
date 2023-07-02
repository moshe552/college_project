from person import Person


class Student(Person):

    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)
        self.__grades = {}
        self.__courses = []

    @property
    def grades(self):
        return self.__grades
