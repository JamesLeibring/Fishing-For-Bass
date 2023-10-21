# Function to draw the unit onto the screen
def draw(self, screen, center, blink=False):
    if blink:
        color = (192, 192, 192)
    else:
        color = self.owner.getColor()

    pygame.draw.circle(screen, (0, 0, 0), center, 16)
    circle = pygame.draw.circle(screen, color, center, 14)
    screen.blit(self.image, circle.topleft)

class Warrior(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/warrior.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Warrior"
        self.total_power = self.power = 1
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Horseman(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/horseman.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Horseman"
        self.total_power = self.power = 1
        self.total_movement = self.movement = 2
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Swordsman(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/swordsman.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Swordsman"
        self.total_power = self.power = 2
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Knight(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/knight.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Knight"
        self.total_power = self.power = 2
        self.total_movement = self.movement = 2
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']
        self.values = [self.power, self.movement]


class Musketman(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/musketman.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Musketman"
        self.total_power = self.power = 3
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Cavalry(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/cavalry.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Cavalry"
        self.total_power = self.power = 3
        self.total_movement = self.movement = 2
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Infantry(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/infantry.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Infantry"
        self.total_power = self.power = 5
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Tank(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/tank.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Tank"
        self.total_power = self.power = 10
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\power', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Archer(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/archer.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Archer"
        self.total_power = self.power = 2
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.defensive = True
        self.attributes = [r'\defense', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Cannon(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/cannon.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Cannon"
        self.total_power = self.power = 4
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.defensive = True
        self.attributes = [r'\defense', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class Artillery(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/artillery.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Artillery"
        self.total_power = self.power = 7
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.defensive = True
        self.attributes = [r'\defense', r'\movement']

    def getValues(self):
        return [self.power, self.movement]


class AntiAircraft(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/anti-air gun.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Anti-Air Gun"
        self.total_power = self.power = 4
        self.total_movement = self.movement = 1
        self.cost = [0, 0, 0, 0]
        self.defensive = True
        self.antiair = True
        self.attributes = [r'\defense', r'\movement', r'\anti-air']

    def getValues(self):
        return [self.power, self.movement, None]


class Ship(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.total_capacity = 0
        self.capacity = 0
        self.boarded_units = []
        self.naval = False
        self.aquatic = True

    def getTotalCapacity(self):
        return self.total_capacity

    def getCapacity(self):
        return self.capacity

    def getBoarded(self):
        return self.boarded_units

    def isNaval(self):
        return self.naval

    # Embarks un into this object
    def embark(self, un):
        self.capacity -= un.getPower()
        self.boarded_units.append(un)
        un.embarked = True

    def disembark(self, un):
        self.capacity += un.getPower()
        self.boarded_units.remove(un)
        un.embarked = False


class Trireme(Ship):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/trireme.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Trireme"
        self.total_power = self.power = 1
        self.total_movement = self.movement = 2
        self.total_capacity = self.capacity = 2
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\aquatic', r'\movement', r'\capacity']

    def getValues(self):
        return [self.power, self.movement, self.capacity]


class Caravel(Ship):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/caravel.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Caravel"
        self.total_power = self.power = 2
        self.total_movement = self.movement = 3
        self.total_capacity = self.capacity = 5
        self.naval = True
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\aquatic', r'\movement', r'\capacity', r'\naval']

    def getValues(self):
        return [self.power, self.movement, self.capacity, None]


class Battleship(Ship):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/battleship.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Battleship"
        self.total_power = self.power = 5
        self.total_movement = self.movement = 4
        self.total_capacity = self.capacity = 6
        self.naval = True
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\aquatic', r'\movement', r'\capacity', r'\naval']

    def getValues(self):
        return [self.power, self.movement, self.capacity, None]


class AircraftCarrier(Ship):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/aircraft carrier.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Aircraft Carrier"
        self.total_power = self.power = 10
        self.total_movement = self.movement = 2
        self.total_capacity = self.capacity = 12
        self.range = 2
        self.carrier = True
        self.defensive = True
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\aquadef', r'\movement', r'\capacity', r'\carrier']
        
    def getRange(self):
        return self.range

    def getValues(self):
        return [self.power, self.movement, self.capacity, None]


class Plane(Unit):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.range = 0
        self.arial = True

    def getRange(self):
        return self.range


class Fighter(Plane):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/fighter.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Fighter"
        self.total_power = self.power = 1
        self.total_movement = self.movement = 1
        self.range = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\arial', r'\movement', r'\range']

    def getValues(self):
        return [self.power, self.movement, self.range]


class Bomber(Plane):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/bomber.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Bomber"
        self.total_power = self.power = 2
        self.total_movement = self.movement = 1
        self.range = 1
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\arial', r'\movement', r'\range']

    def getValues(self):
        return [self.power, self.movement, self.range]


class JetFighter(Plane):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/jet fighter.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Jet Fighter"
        self.total_power = self.power = 3
        self.total_movement = self.movement = 1
        self.range = 2
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\arial', r'\movement', r'\range']

    def getValues(self):
        return [self.power, self.movement, self.range]


class Helicopter(Plane):
    def __init__(self, owner, location):
        super().__init__(owner, location)
        self.image = pygame.image.load(os.getcwd() + "/images/helicopter.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.name = "Helicopter"
        self.total_power = self.power = 1
        self.total_movement = self.movement = 1
        self.total_capacity = self.capacity = 5
        self.range = 2
        self.boarded_units = []
        self.cost = [0, 0, 0, 0]
        self.attributes = [r'\arial', r'\movement', r'\range', r'\capacity']

    def getValues(self):
        return [self.power, self.movement, self.range, self.capacity]

    def getTotalCapacity(self):
        return self.total_capacity

    def getCapacity(self):
        return self.capacity

    def getBoarded(self):
        return self.boarded_units

    # Embarks un into this object
    def embark(self, un):
        self.capacity -= un.getPower()
        self.boarded_units.append(un)
        un.embarked = True

    def disembark(self, un):
        self.capacity += un.getPower()
        self.boarded_units.remove(un)
        un.embarked = False


def make_unit(name, owner=None, loc=None):
    if name == "Warrior":
        return Warrior(owner, loc)
    elif name == "Horseman":
        return Horseman(owner, loc)
    elif name == "Swordsman":
        return Swordsman(owner, loc)
    elif name == "Knight":
        return Knight(owner, loc)
    elif name == "Musketman":
        return Musketman(owner, loc)
    elif name == "Cavalry":
        return Cavalry(owner, loc)
    elif name == "Infantry":
        return Infantry(owner, loc)
    elif name == "Tank":
        return Tank(owner, loc)
    elif name == "Archer":
        return Archer(owner, loc)
    elif name == "Cannon":
        return Cannon(owner, loc)
    elif name == "Artillery":
        return Artillery(owner, loc)
    elif name == "Anti-Air Gun":
        return AntiAircraft(owner, loc)
    elif name == "Trireme":
        return Trireme(owner, loc)
    elif name == "Caravel":
        return Caravel(owner, loc)
    elif name == "Battleship":
        return Battleship(owner, loc)
    elif name == "Aircraft Carrier":
        return AircraftCarrier(owner, loc)
    elif name == "Fighter":
        return Fighter(owner, loc)
    elif name == "Bomber":
        return Bomber(owner, loc)
    elif name == "Jet Fighter":
        return JetFighter(owner, loc)
    elif name == "Helicopter":
        return Helicopter(owner, loc)
    return None
