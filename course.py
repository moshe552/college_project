class Course:
    id_auto_increment = 1

    def __init__(self, name):
        self.__name = name
        self.__id = Course.id_auto_increment
        self.__teacher_id = 0
        self.students = {}
        Course.id_auto_increment += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def teacher_id(self):
        return self.__teacher_id

    @teacher_id.setter
    def teacher_id(self, new_teacher_id):
        self.__teacher_id = new_teacher_id

    def __str__(self):
        return "ID: " + str(self.id) + ", Name: " + self.name
