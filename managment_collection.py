class ManagementCollection:
    """
    A collection of methods for dict management.
    """
    def __init__(self):
        self.dict_of_items = {}

    def add(self, instance):
        self.dict_of_items[instance.id] = instance

    def adding(self, instance, dictionary: dict):
        dictionary[instance.id] = instance

    def get(self, instance_id: int):
        return self.dict_of_items[instance_id]

    def remove(self, instance_id: int):
        del self.dict_of_items[instance_id]

    def removing(self, instance_id: int, dictionary: dict):
        del dictionary[instance_id]






