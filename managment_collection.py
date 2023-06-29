from person import Person


class ManagementCollection:
    """
    A collection of methods for dict management.
    """
    def __init__(self):
        self.__dict = {}

    def add(self, person: Person):
        self.__dict[person.id] = person

    def get(self, person):
        return person  # to use the __reaper__ in order to get all the details.

    def remove(self, person):
        del self.__dict[person.id]

    def print_all(self, _id):
        print(self.__dict[_id])  # to use __reaper__ or __str__


