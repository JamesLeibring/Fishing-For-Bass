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

#------------------------------------------------------------------------------------

def advanceTurn(self, turn):
    for ter in self.territories:
        if ter.isClaimed(turn):
            for i, res in enumerate(ter.getResources()):
                self.resources[i] += res

def createUnitQueue(self):
    unit_queue = []
    for un in self.units:
        un.movement = un.total_movement
        if not un.isFortified() and not un.isEmbarked():
            for mov in range(un.movement):
                unit_queue.append(un)
    return unit_queue

def purchaseUnit(self, loc, un, isCoast):
    if isCoast and loc not in self.coasts:
        self.coasts.append(loc)
    for i, cost in enumerate(un.getCost()):
        self.resources[i] -= cost
    self.units.append(un)
    loc.purchaseUnit(un)

def move(self, loc, un, turn, isCoast):
    old_loc = un.getLocation()
    # The move_from function moves the unit from there, returning True if the territory is now Empty
    if old_loc.move_from(un):
        if isCoast:
            self.coasts.remove(old_loc)
        else:
            self.territories.remove(old_loc)

    # The move_to function moves the unit to the new loc, returning True if the territory was Empty
    if loc.move_to(un):
        if isCoast:
            self.coasts.append(loc)
        else:
            self.territories.append(loc)
            loc.turn_claimed = turn

    # If the unit has passengers we move them with the unit
    if un.isAquatic() or type(un) == unit.Helicopter:
        for i in range(len(un.getBoarded())):
            brd = un.getBoarded()[i]
            self.move(loc, brd, turn, isCoast)

def attack(self, loc, un, turn, isCoast):
    # We can determine the winner of the fight before we even fight!
    def_pow = loc.getPower()
    att_pow = un.getPower()
    conquered = att_pow > def_pow

    # Now that the attacker has been situated, its time to take our toll on the defending location
    loc.defend(att_pow)

    # If the attacker would die, then it dies. If not, then subtract any damage it would survive and move it in
    if not conquered:
        self.loseUnit(un.getLocation(), un)
    else:
        un.takeDamage(def_pow)
        self.move(loc, un, turn, isCoast)

    return conquered

# Performs an Arial Attack. Returns true if the defending ter had an anti air gun
def arialAttack(self, ter, un, turn):
    if type(un) == unit.AircraftCarrier:
        for i in range(len(un.getBoarded())):
            brd = un.getBoarded()[i]
            if brd.isArial():
                self.arialAttack(ter, brd, turn)
        return False

    att_pow = un.getPower()
    # If there is ant Anti Air gun then the plane is gunned down
    if True in [x.isAntiAir() for x in ter.getUnits()]:
        self.loseUnit(un.getLocation(), un)
        return True

    ter.defend(att_pow)

    if type(un) == unit.Helicopter:
        cpy_boarded = un.getBoarded()
        for brd in cpy_boarded:
            self.disembark(un, ter, brd, turn)
    return False

# If a unit dies in combat, it is handled here
def loseUnit(self, ter, un):
    is_empty = ter.loseUnit(un)
    self.units.remove(un)
    if is_empty and type(un.getLocation()) == location.Coast:
        self.coasts.remove(ter)
    elif is_empty:
        self.territories.remove(ter)
    # If the unit that died had units in it, they will be killed as well :(
    if un.isAquatic() or type(un) == unit.Helicopter:
        for i in range(len(un.getBoarded())):
            brd = un.getBoarded()[i]
            self.loseUnit(ter, brd)

def embark(self, ship, un):
    old_loc = un.getLocation()
    if old_loc.move_from(un):
        self.territories.remove(old_loc)
    ship.getLocation().move_to(un)

    if type(un) == unit.Helicopter:
        for i in range(len(un.getBoarded())):
            brd = un.getBoarded()[i]
            if old_loc.move_from(brd):
                self.territories.remove(old_loc)
            ship.getLocation().move_to(brd)

    ship.embark(un)

def disembark(self, ship, ter, un, turn):
    un_alive = True

    # If it is our territory
    if ter.getOwner() is not None and ter.getOwner() != self:
        def_pow = ter.getPower()
        att_pow = un.getPower()

        ter.defend(att_pow)

        if att_pow <= def_pow:
            self.loseUnit(un.getLocation(), un)
            un_alive = False
        else:
            un.takeDamage(def_pow)

    ship.disembark(un)

    # If the unit is alive after attacking the ter, move it into the ter!
    if un_alive:
        ship.getLocation().move_from(un)

        if ter.move_to(un):
            self.territories.append(ter)
            ter.turn_claimed = turn

        # If the unit has passengers we move them with the unit
        if type(un) == unit.Helicopter:
            for i in range(len(un.getBoarded())):
                brd = un.getBoarded()[i]
                ship.getLocation().move_from(brd)
                un.getLocation().move_to(brd)


# Draw the units for the territory, if unit is specified it means that units turn is up.
def draw(self, screen, un=None, blink=False):
    black = (0, 0, 0)
    grey = (100, 100, 100)
    font = pygame.font.Font('freesansbold.ttf', 9)
    # Now we draw the power indicator
    power = font.render(roman(self.power), True, black, grey)
    txt_rect = power.get_rect()
    txt_rect.center = (self.center[0] - 16, self.center[1] - 16)
    pygame.draw.circle(screen, black, txt_rect.center, 13)
    pygame.draw.circle(screen, grey, txt_rect.center, 11)
    screen.blit(power, txt_rect)
    # If there is more than one unit, then also show the power and size of the stack
    if len(self.units) > 1:
        # Draw the number showing how many units there are in the stack
        mul = font.render("x" + str(len(self.units)), True, black, grey)
        txt_rect = mul.get_rect()
        txt_rect.center = (self.center[0] + 15, self.center[1] - 16)
        pygame.draw.circle(screen, black, txt_rect.center, 11)
        pygame.draw.circle(screen, grey, txt_rect.center, 9)
        screen.blit(mul, txt_rect)
    # Drawing the actual unit.
    if un in self.units:
        un.draw(screen, self.center, blink)
    else:
        self.units[0].draw(screen, self.center)