
class Item:
    def __init__(self, shelving_id, item_type_id, position, code, name, is_active, description = None):
        self.shelving_id = shelving_id
        self.item_type_id = item_type_id
        self.position = position
        self.code = code
        self.name = name
        self.is_active = is_active
        self.description = description