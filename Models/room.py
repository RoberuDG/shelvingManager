

class Room:
    def __init__(self, name, positions, description=None, id = None):
        self.id = id
        self.name = name
        self.positions = positions
        self.description = description
