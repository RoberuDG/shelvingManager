
class Item:
    def __init__(self, shelf_id, item_type_id, name, position, description=None, id = None):
        self.id = id
        self.shelf_id = shelf_id
        self.item_type_id = item_type_id
        self.position = position
        self.name = name
        self.description = description
