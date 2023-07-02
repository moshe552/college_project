class ManagementCollection:
    """
    A collection of methods for dict management.
    """
    def __init__(self):
        self.dict_of_things = {}

    @property
    def dict(self):
        return self.dict_of_things

    def add(self, instance):
        self.dict[instance.id] = instance

    def get(self, instance):
        return self.dict[instance]

    def remove(self, instance):
        del self.dict[instance]

    def print_all(self, id_):
        print(self.dict[id_])



