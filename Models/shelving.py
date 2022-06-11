
class Shelving:
    def __init__(self, room_id, code, position, description = None, id = None):
        self.id = id
        self.room_id = room_id
        self.code = code
        self.position = position
        self.description = description
