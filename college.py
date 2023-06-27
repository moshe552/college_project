class College:

    def __init__(self, name):
        self.__name = name
        self.students = []
        self.teachers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

