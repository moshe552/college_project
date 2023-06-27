from person import Person


class Teachers(Person):

    def __init__(self, name, phone, email, lst):
        super().__init__(name, phone, email)
        lst.append(self)
