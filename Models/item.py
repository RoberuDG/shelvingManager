
class Item:
    def __init__(self, shelve_id, item_type_id, position, name, is_active, description = None):
        self.shelve_id = shelve_id
        self.item_type_id = item_type_id
        self.position = position
        self.name = name
        self.is_active = is_active
        self.description = description