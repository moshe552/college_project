class ManagementCollection:
    """
    A collection of methods for dict management.
    """
    def __init__(self):
        self.dict_of_items = {}

    def add(self, instance):
        self.dict_of_items[instance.id] = instance

    def add_2_arguments(self, instance, dictionary: dict):
        dictionary[instance.id] = instance

    def get(self, item_id: int):
        return self.dict_of_items[item_id]

    def remove(self, item_id: int):
        del self.dict_of_items[item_id]

    def remove_2_arguments(self, instance_id: int, dictionary: dict):
        del dictionary[instance_id]

    def show_person_courses(self, person_id):
        person_instance = self.get(person_id)
        for val in person_instance.courses.values():
            print(val.name)

    def valid_item(self, item_id):
        if item_id not in self.dict_of_items:
            return False
        return True

    def print_items(self):
        for item in self.dict_of_items.values():
            print(item)
