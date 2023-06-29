from person import Person


class Student(Person):

    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)

