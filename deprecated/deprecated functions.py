# Function to draw the unit onto the screen
def draw(self, screen, center, blink=False):
    if blink:
        color = (192, 192, 192)
    else:
        color = self.owner.getColor()

    pygame.draw.circle(screen, (0, 0, 0), center, 16)
    circle = pygame.draw.circle(screen, color, center, 14)
    screen.blit(self.image, circle.topleft)

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

"""
    # Called within a while loop, updates the game state and visual state for the user
    def update(self, player_num, msg=None):
        # The return value for the update function. This is not None when some significant occurs during the game tick
        ret_val = None

        # This parses your opponents turns! Anything they do will be run here :)
        if msg is not None:
            self.parseMessage(msg)

        # Find how much time has lapsed so far
        time_lapsed = time.time() - self.startTime

        # Redraw the screens for the new game image
        self.screen.blit(self.clear_screen, (0, 0))
        self.clear_screen.blit(self.map, (20, 20))

        # The hov variable represents the area of the map our mouse is located in
        hov = self.hover(x, y)

        # Check our users actions to determine changes in game state
        for event in pygame.event.get():
            # If we click the X button, then close the screen
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'exit'
            # If we notice a left click and it is our turn, then determine what the click was
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # If we clicked somewhere on the map go here
                if self.mapRect.collidepoint(x, y) and not self.inInfo and player_num == self.playerNum:
                    if self.gameStart(hov):
                        ret_val = self.startGame(self.pc, hov)
                    elif self.placeUnit(hov):
                        ret_val = self.purchaseUnit(self.pc, hov, self.unitPurchased)
                        self.drawShop(self.pc.getColor())
                    elif self.canMove(hov):
                        ret_val = self.move(self.pc, hov, self.unitQueue[0])
                    elif self.canNavigate(hov):
                        self.unitQueue.pop(0)
                        tmp = self.unitQueue.pop(0)
                        tmp.movement -= 2
                        ret_val = self.move(self.pc, hov, self.unitQueue[0])
                    elif self.canAttack(hov):
                        ret_val = self.attack(self.pc, hov, self.unitQueue[0])
                    elif self.canUnfortify(hov):
                        self.unfortify(hov)
                    elif self.wikiRect.collidepoint(x, y):
                        self.inInfo = True
                # If we clicked somewhere in the shop go here instead
                elif self.shopRect.collidepoint(x, y) and not self.inInfo and player_num == self.playerNum:
                    if self.canPurchase(hov):
                        self.unitPurchased = hov
                        self.drawShop(self.c["dark_grey"])
                    elif self.canEmbark(hov):
                        ret_val = self.embark(self.pc, hov, self.unitQueue[0])
                        self.shopChoices = self.drawShop(self.pc.getColor())
                    elif self.canDisembark(hov):
                        ret_val = self.disembark(self.pc, self.unitQueue[0], hov)
                        self.shopChoices = self.drawShop(self.pc.getColor())
                # This controls us in the Game Info Page
                elif self.mapRect.collidepoint(x, y) and self.inInfo:
                    if self.wikiRect.collidepoint(x, y):
                        self.inInfo = False
            # If the event type is instead a right click (as used by arial units), handle actions hre instead
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if self.mapRect.collidepoint(x, y) and not self.inInfo and player_num == self.playerNum:
                    if self.canArialAttack(hov):
                        ret_val = self.arialAttack(self.pc, hov, self.unitQueue[0])
            # Handles key events like fortiy (f) and skip unit turn (space)
            elif event.type == pygame.KEYDOWN and not self.inInfo and player_num == self.playerNum:
                if event.key == pygame.K_SPACE:
                    self.skipTurn()
                elif event.key == pygame.K_f:
                    self.fortify()
                elif event.key == pygame.K_RETURN:
                    ret_val = self.endTurn()
                elif event.key == pygame.K_e:
                    if self.canBoard():
                        self.prepareEmbark()
                        self.shopChoices = self.drawBoarding()
                elif event.key == pygame.K_d:
                    if self.canUnBoard():
                        self.prepareDisembark()
                        self.shopChoices = self.drawBoarding()
        # Now we edit anything that may need to be drawn
        if not self.inInfo:
            self.drawGame(hov, time_lapsed, player_num)
        else:
            self.drawWiki()
        self.drawWikiCirc()

        # Update our computer screen with the newly created screen visuals
        pygame.display.update()

        # Return our action, weather it be None or something of importance
        return ret_val

    # BOOLEANS : Helper Booleans to determine what action the user is taking
    # -----------------------------------------------------------------------

    # This returns true so long as the player is not waiting on any specific actions to occur
    # For example, when we but a unit we ned to place it before doing anything else
    def notWaiting(self, hov):
        return hov and not self.unitPurchased and not self.unitBoarding and self.turn > 0

    # Returns true if the location given is owned by the enemy
    def isEnemy(self, hov):
        return hov.getOwner() != self.pc and hov.getOwner() is not None

    # Returns true if the location given is owned by the pc
    def isAlly(self, hov):
        return hov.getOwner() == self.pc

    # Returns true if the hovered location is neighboring the unit up
    def isNeighbor(self, hov):
        return hov and self.unitQueue and hov.getName() in self.unitQueue[0].getLocation().getNeighbors()

    # Function to determine if the game start for this player has all of its conditions met
    def gameStart(self, hov):
        return self.turn == 0 and hov and not self.isEnemy(hov) and len(self.pc.getUnits()) == 0

    # If the player can purchase the unit hovered, thn return True
    def canPurchase(self, hov):
        if self.notWaiting(hov) and hov in self.units and not self.boardableUnits:
            return not (False in [x >= y for x, y in zip(self.pc.getResources(), hov.getCost())])
        return False

    # If the player places the unit purchased, returns True
    def placeUnit(self, hov):
        if hov and self.unitPurchased and not self.unitBoarding:
            if self.unitPurchased.isAquatic():
                return self.isAlly(hov.getCoast()) or (hov.getCoast().getOwner() is None and self.isAlly(hov))
            else:
                return self.isAlly(hov)

    # If there are units fortified, returns True
    def canUnfortify(self, hov):
        return self.notWaiting(hov) and (self.isAlly(hov) or self.isAlly(hov.getCoast()))

    # If the unit can move to the hovered territory, then do so
    def canMove(self, hov):
        if self.notWaiting(hov) and self.isNeighbor(hov):
            if self.unitQueue[0].isAquatic():
                return not self.isEnemy(hov.getCoast())
            else:
                return not self.isEnemy(hov)
        return False

    # If the unit can navigate now, returns True
    def canNavigate(self, hov):
        if self.notWaiting(hov) and not self.isEnemy(hov.getCoast()) and len(self.unitQueue) >= 3:
            return self.unitQueue[0].isAquatic() and self.unitQueue[0] == self.unitQueue[1] == self.unitQueue[2]
        return False

    # Determines if the player is attacking another unit
    def canAttack(self, hov):
        if self.notWaiting(hov) and self.isNeighbor(hov) and not self.unitQueue[0].isDefensive():
            if self.unitQueue[0].isAquatic():
                return self.isEnemy(hov.getCoast())
            else:
                return self.isEnemy(hov)
        return False

    # Determines if the unit up can Arial Attack the hovered area
    def canArialAttack(self, hov):
        return self.notWaiting(hov) and self.isEnemy(hov) and self.unitQueue and self.inRange(hov)

    # Determines if the territory is in range of an arial units attack!
    def inRange(self, ter):
        if not (self.unitQueue[0].isArial() or type(self.unitQueue[0]) == unit.AircraftCarrier):
            return False
        un = self.unitQueue[0]
        rng = un.getRange()

        if rng == 0:
            return False

        loc = un.getLocation()        
        if type(loc) == location.Coast:
            loc = loc.getTerritory()
        neighbors = loc.getNeighbors() + loc.getCoast().getNeighbors()

        if ter.getName() == loc.getName() and ter.getOwner() != self.pc:
            return True
        elif rng == 1:
            return ter.getName() in neighbors
        elif rng == 2:
            for nei in neighbors:
                if nei in ter.getNeighbors() + ter.getCoast().getNeighbors():
                    return True
        return False

    # The board button prepares a unit to be boarded, if it works unitBoarded will be set
    def canBoard(self):
        if self.unitQueue and not self.unitPurchased and not self.unitBoarding:
            loc = self.unitQueue[0].getLocation()
            # Check for ships
            if loc.getName() != "Irkutsk" and type(loc) == location.Territory and self.isAlly(loc.getCoast()):
                return True in [self.canFit(x) for x in loc.getCoast().getUnits()]
            # Check for helicopters
            return True in [self.canFit(x) for x in loc.getUnits()]
        return False

    # Returns Tue if there is a unit that can disembark. Units require movement to disembark
    def canUnBoard(self):
        if self.unitQueue and not self.unitPurchased and not self.unitBoarding:
            un = self.unitQueue[0]
            loc = un.getLocation()
            if type(un) == unit.Helicopter:
                return un.getBoarded() and (True in [x.getMovement() > 0 for x in un.getBoarded()])
            elif un.isAquatic() and not self.isEnemy(loc.getTerritory()) or un.isNaval():
                return un.getBoarded() and (True in [x.getMovement() > 0 for x in un.getBoarded()])
        return False

    def canEmbark(self, hov):
        return self.boardableUnits and hov in self.boardableUnits and self.unitBoarding and not self.unitPurchased

    def canDisembark(self, hov):
        return self.notWaiting(hov) and self.boardableUnits and hov in self.boardableUnits

    # Can fit takes in two units and decides if the first could board the second
    def canFit(self, ship):
        un = self.unitQueue[0]
        if type(ship) == unit.AircraftCarrier:
            return not un.isAquatic() and ship.getCapacity() >= un.getPower()
        elif ship.isAquatic():
            return not un.isAquatic() and not un.isArial() and ship.getCapacity() >= un.getPower()
        elif type(ship) == unit.Helicopter:
            return not un.isAquatic() and not un.isArial() and ship.getCapacity() >= un.getPower() and not un.isDefensive()

        return False

    # ACTIONS : Helper functions to take the actual action specified
    # -----------------------------------------------------------------------

    # Advances all players turns, both granting them resources and making a unitQueue, which handles unit turns
    def advanceTurn(self):
        self.turn += 1
        self.drawTurn(0)
        for pl in self.players:
            pl.advanceTurn(self.turn)
        self.drawResources(self.resourceNames, self.pc.resources, self.resourceRect)

    def createUnitQueue(self):
        self.unitQueue = self.pc.createUnitQueue()

    # Starts the game for the player mentioned, they will automatically be granted a Warrior on ter
    def startGame(self, pl, ter):
        pl.startGame(ter, unit.make_unit("Warrior", pl, ter))
        if pl == self.pc:
            return [0, self.playerNum, self.territories.index(ter)]

    # Purchases the unit and places them in ter (NOTE : ter could be both a territory or coast)
    def purchaseUnit(self, pl, ter, un):
        if un.isAquatic():
            un_ = unit.make_unit(un.getName(), pl, ter.getCoast())
            pl.purchaseUnit(ter.getCoast(), un_, True)
        else:
            un_ = unit.make_unit(un.getName(), pl, ter)
            pl.purchaseUnit(ter, un_, False)
        if pl == self.pc:
            self.unitPurchased = None
            return [1, self.playerNum, self.territories.index(ter), self.units.index(un)]

    # If the user presses the space bar, the current unit waives their turn
    def skipTurn(self):
        if self.unitQueue and not self.unitPurchased and not self.unitBoarding and self.turn > 0:
            tmp = self.unitQueue.pop(0)
            while self.unitQueue and tmp == self.unitQueue[0]:
                tmp = self.unitQueue.pop(0)
            tmp.movement = 0

    # The fortify is like a more advanced space bar. It tells the game to waive your turn for all turns until unfortified
    def fortify(self):
        if self.unitQueue and not self.unitPurchased and not self.unitBoarding:
            tmp = self.unitQueue.pop(0)
            while self.unitQueue and tmp == self.unitQueue[0]:
                tmp = self.unitQueue.pop(0)
            tmp.fortified = True

    # Unfortifies any units in the hovered territory/coast
    def unfortify(self, hov):
        if hov in self.pc.getTerritories():
            for un in hov.getUnits():
                if un.isFortified():
                    for i in range(un.getMovement()):
                        self.unitQueue.append(un)
                    un.fortified = False
        if hov.getCoast() in self.pc.getCoasts():
            for un in hov.getCoast().getUnits():
                if un.isFortified():
                    for i in range(un.getMovement()):
                        self.unitQueue.append(un)
                    un.fortified = False

    # The enter button waives our turn.
    def endTurn(self):
        if not self.unitPurchased and not self.unitBoarding:
            return [7]

    # Player moves un to ter (NOTE : ter could be both a territory or coast)
    def move(self, pl, ter, un):
        if un.isAquatic():
            pl.move(ter.getCoast(), un, self.turn, True)
        else:
            pl.move(ter, un, self.turn, False)
        if pl == self.pc:
            tmp = self.unitQueue.pop(0)
            tmp.movement -= 1
            return [2, self.playerNum, self.territories.index(ter), self.pc.getUnits().index(un)]

    # The attack function attacks ter with un owned by pl
    def attack(self, pl, ter, un):
        # player attack function returns true if the unit attacking defeated the ter and moves in
        ret_val = [3, self.playerNum, self.territories.index(ter), pl.getUnits().index(un)]

        if un.isAquatic():
            ter = ter.getCoast()

        # Do the attack, if the territory is destroyed and the unit survives, then this is True
        conquered_ter = pl.attack(ter, un, self.turn, un.isAquatic())

        # Attacking costs a movement, but if the unit died we should remove it from the unit queue
        if pl == self.pc:
            tmp = self.unitQueue.pop(0)
            tmp.movement -= 1
            if not conquered_ter:
                while tmp.movement > 0:
                    self.unitQueue.pop(0)
                    tmp.movement -= 1
            return ret_val

    # Performs an Arial Attack!
    def arialAttack(self, pl, ter, un):
        ret_val = [4, self.playerNum, self.territories.index(ter), pl.getUnits().index(un)]

        gunned_down = pl.arialAttack(ter, un, self.turn)

        if pl == self.pc:
            tmp = self.unitQueue.pop(0)
            tmp.movement -= 1
            if gunned_down:
                while tmp.movement > 0:
                    self.unitQueue.pop(0)
                    tmp.movement -= 1
            return ret_val

    # Get our class variables ready to board
    def prepareEmbark(self):
        self.unitBoarding = self.unitQueue[0]
        copters = [un_ for un_ in self.unitQueue[0].getLocation().getUnits() if type(un_) == unit.Helicopter]
        self.boardableUnits = [ship for ship in copters + self.unitQueue[0].getLocation().getCoast().getUnits() if
                               self.canFit(ship)]

    def prepareDisembark(self):
        self.boardableUnits = [un for un in self.unitQueue[0].getBoarded() if un.getMovement() > 0]

    # Embarks un onto ship!
    def embark(self, pl, ship, un):
        ret_val = [5, self.playerNum, pl.getUnits().index(ship), pl.getUnits().index(un)]

        pl.embark(ship, un)

        if pl == self.pc:
            tmp = self.unitQueue.pop(0)
            tmp.movement -= 1
            while self.unitQueue and self.unitQueue[0] == tmp:
                self.unitQueue.pop(0)

            self.boardableUnits = None
            self.unitBoarding = None
            return ret_val

    def disembark(self, pl, ship, un):
        ret_val = [6, self.playerNum, pl.getUnits().index(ship), pl.getUnits().index(un)]

        # Returns True is the disembarking unit died while doing so
        if ship.isAquatic():
            dead = pl.disembark(ship, ship.getLocation().getTerritory(), un, self.turn)
        else:
            dead = pl.disembark(ship, ship.getLocation(), un, self.turn)

        if pl == self.pc:
            if not dead and un.movement > 0:
                for mov in range(un.movement - 1):
                    self.unitQueue.append(un)
                un.movement -= 1
            self.boardableUnits = None
            return ret_val
"""