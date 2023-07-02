from person import Person


class Teacher(Person):

    def __init__(self, name, phone, email, salary):
        super().__init__(name, phone, email)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
