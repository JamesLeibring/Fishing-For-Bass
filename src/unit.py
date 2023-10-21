# The Unit Class : Describes a unit in its entirity

class Unit:
    def __init__(self):
        self.power = 0
        self.movement = 0

class DefensiveUnit(Unit):
    def __init__(self):
        super().__init__()

        self.defense = 0

class CapacityUnit(Unit):
    def __init__(self):
        super().__init__()
        
        self.capacity = 0

class RangedUnit(Unit):
    def __init__(self):
        super().__init__()

        self.range = 0

class LandUnit(Unit):
    def __init__(self):
        super().__init__()
        pass

class SeaUnit(Unit):
    def __init__(self):
        super().__init__()
        pass

class AirUnit(Unit):
    def __init__(self):
        super().__init__()
        pass
