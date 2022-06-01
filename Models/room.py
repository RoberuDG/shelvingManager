

class Habitacion:
    def __init__(self, name, positions, creation_date, description = None):
        self.name = name
        self.positions = positions
        self.creation_date = creation_date
        self.description = description
    
    def get_habitaciones_from_model(__name: str) -> Habitacion:
        pass