# The Player Class

class Player:
    def __init__(self, player_number):
        self.territories = []
        self.coasts = []
        self.units = []
        self.resources = [0, 0, 0, 0]
        # The color associated with your player varies
        if player_number == 0:
            self.color = (173, 0, 0)
            self.highlight = (173, 20, 20, 1)
        elif player_number == 1:
            self.color = (0, 153, 0)
            self.highlight = (20, 153, 20, 1)
        elif player_number == 2:
            self.color = (0, 0, 153)
            self.highlight = (30, 30, 160, 1)
        elif player_number == 3:
            self.color = (0, 153, 153)
            self.highlight = (20, 153, 153, 1)
        elif player_number == 4:
            self.color = (153, 0, 153)
            self.highlight = (153, 20, 153, 1)
        elif player_number == 5:
            self.color = (153, 153, 0)
            self.highlight = (153, 153, 20, 1)
        else:
            self.color = (100, 100, 100)
            self.highlight = (100, 100, 100, 3)

    # Draws in any units or territories owned by this player
    def draw(self, screen, turn, un=None, blink=False):
        for ter in self.territories:
            if ter.isClaimed(turn):
                pygame.draw.polygon(screen, self.highlight, ter.getBorder())
            ter.draw(screen, un, blink)
        for cst in self.coasts:
            cst.draw(screen, un, blink)

    # ACTIONS : Actions taken by the player are often delegated to the player class, we take them in these functions
    # -----------------------------------------------------------------------

    def startGame(self, ter, un):
        self.territories.append(ter)
        self.units.append(un)
        ter.startGame(self, un)

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
