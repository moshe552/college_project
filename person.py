from managment_collection import ManagementCollection


class Person(ManagementCollection):
    """
    Creates all the properties and methods necessary for a person in college.
    """
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.__email = email
