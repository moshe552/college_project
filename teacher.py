from person import Person


class Teachers(Person):

    def __init__(self, name, phone, email, salary):
        super().__init__(name, phone, email)
        self.__salary = salary

