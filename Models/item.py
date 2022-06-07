
class Item:
    def __init__(self, id, shelve_id, item_type_id, position, name, description=None):
        self.id = id
        self.shelve_id = shelve_id
        self.item_type_id = item_type_id
        self.position = position
        self.name = name
        self.description = description
