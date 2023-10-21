3 # The Location Class

class Location:
    # Constructor
    def __init__(self, name):
        self.name = name
        
        self.power = 0
        self.units = []

    # ACTIONS : Sometimes even our territory values must be changed when Actions occur, we do this in these functions
    # -----------------------------------------------------------------------

    # For when a unit is bought and placed here
    def purchaseUnit(self, un):
        self.power += un.getPower()
        self.units.append(un)
        self.owner = un.getOwner()

    def move_from(self, un):
        self.power -= un.getPower()
        self.units.remove(un)
        if len(self.units) == 0:
            self.owner = None
            return True
        return False

    def move_to(self, un):
        self.power += un.getPower()
        self.units.append(un)
        un.move(self)
        if len(self.units) == 1:
            self.owner = un.getOwner()
            return True
        return False

    # Function to defend from player pl's attacking unit un
    def defend(self, att_pow):
        # So long as the attacking power is not brought to 0, then the defenders will keep fighting
        while att_pow > 0 and self.power > 0:
            # Trade the first unit
            defender = self.units[0]
            def_pow = defender.getPower()

            # If the defender is stronger, then it just takes the damage
            if def_pow > att_pow:
                defender.takeDamage(att_pow)
            # If not then it will die
            else:
                self.owner.loseUnit(self, defender)
            att_pow -= def_pow

    def loseUnit(self, un):
        self.power -= un.getPower()
        self.units.remove(un)
        if len(self.units) == 0:
            self.owner = None
            return True
        return False


class Coast(Location):
    def __init__(self, name, data, ter):
        super().__init__(name, data["sea_neighbors"], data["sea_button"])
        self.territory = ter

    def getTerritory(self):
        return self.territory

    def navPower(self):
        return sum([un.getPower() for un in self.units])


class Territory(Location):
    def __init__(self, name, data):
        super().__init__(name, data["neighbors"], data["button"].center)
        self.coast = Coast(name, data, self)
        self.button = data["button"]
        self.border = data["border"]
        self.resources = data["resources"]
        self.turn_claimed = None

    def getCoast(self):
        return self.coast

    def getButton(self):
        return self.button

    def getBorder(self):
        return self.border

    def getResources(self):
        return self.resources

    def isClaimed(self, turn):
        if self.turn_claimed is not None:
            return self.turn_claimed == 0 or self.turn_claimed <= turn - 3
        return False

    def attPower(self):
        return sum([un.getPower() for un in self.units if not un.isDefensive() and not un.isArial()])

    def defPower(self):
        return sum([un.getPower() for un in self.units if un.isDefensive()])

    def ariPower(self):
        return sum([un.getPower() for un in self.units if un.isArial()])

    # ACTIONS : Sometimes even our territory values must be changed when Actions occur, we do this in these functions
    # -----------------------------------------------------------------------

    # Function to begin the game calle by this territories new owner
    def startGame(self, owner, un):
        self.owner = owner
        self.turn_claimed = 0
        self.power += un.getPower()
        self.units.append(un)

    def move_from(self, un):
        if super(Territory, self).move_from(un):
            self.turn_claimed = None
            return True
        return False

    def loseUnit(self, un):
        if super(Territory, self).loseUnit(un):
            self.turn_claimed = None
            return True
        return False


# Turn a integer into a Roman Numeral
def roman(number):
    ret_val = ""
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            ret_val += sym[i]
            div -= 1
        i -= 1
    return ret_val
