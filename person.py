class Person:
    """
    Creates all the properties and methods necessary for a person in college.
    """
    id_auto_increment = 1

    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__id = Person.id_auto_increment
        self.courses = {}
        Person.id_auto_increment += 1

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
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return "id: " + str(self.id) + ", name: " + self.name +\
            ", phone: " + self.phone + ", email: " + self.email
