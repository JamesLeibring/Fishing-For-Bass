import config
import drawer
import player

class Controller:
    def __init__(self, player_count):
        self.config = config.config

        # The Drawer draws everything we need on the screen
        self.drawer = drawer.Drawer(self.config['Drawer'])

        # The Players for this game
        self.players = [player.Player(i) for i in range(player_count)]
        self.pc = 0

        # The territories for this game
        #self.territories = [location.Territory(ter) for ter in self.config['Territories']]

        # The turn the game is on
        self.turn = 0

        # The item the users mouse is hovering over
        self.hov = None

    def gameLoop(self):
        self.drawer.drawBackground(self.pc)

        # Boolean for when the game is running
        running = True

        while running:
            self.draw()

            input()

            running = False

    # Draw the game state
    def draw(self):
        # Draw varying information on the Sidebar
        self.drawer.drawTurn(self.turn)
        self.drawer.drawResources(self.players[self.pc].resources)
        self.drawer.drawShop(self.pc)

        # Draw everything on the map
        self.drawer.drawMap(len(self.players))

        self.drawer.flip()

    # Hover function determines if you are hovering a unit or territory and returns it
    def hover(self, x, y):
        for ter in self.territories:
            if ter.button.collidepoint(x, y):
                return ter
        if not self.boardableUnits:
            for i, rect in enumerate(self.shopChoices):
                if rect.collidepoint(x, y):
                    return self.units[i]
        else:
            for i, rect in enumerate(self.shopChoices):
                if rect.collidepoint(x, y):
                    return self.boardableUnits[i]
        return None
"""
    # Draws any variable visuals to the game, that is, anything that is often changing or variable
    def drawGame(self, hov, time_lapsed, player_up):
        self.drawTurn(player_up)
        # Highlights sections of the map if conditions are met
        if self.notWaiting(hov) and hov in self.territories and not hov.isClaimed(self.turn):
            if not self.unitQueue or hov.getName() in self.unitQueue[0].getLocation().getNeighbors() or self.canNavigate(hov):
                pygame.draw.polygon(self.clear_screen, data.loc_info[hov.getName()]["highlight"], hov.getBorder())
        # Any areas that are owned by players will be colored and any units drawn
        for pl in self.players:
            if pl == self.pc and self.unitQueue and not self.unitPurchased and not self.unitBoarding and player_up == self.playerNum:
                self.pc.draw(self.clear_screen, self.turn, self.unitQueue[0], time_lapsed % 1 < 0.5)
            else:
                pl.draw(self.clear_screen, self.turn)
        # Redraw the info box based on where we are hovered. The info box will display many different helpful stats
        pygame.draw.rect(self.screen, self.c["light_grey"], self.infoRect)
        if hov:
            self.drawInfo(hov)
            # Once the info box is drawn, we also draw draw a bullseye on territories if they are in range of the active unit
            if self.canArialAttack(hov):
                self.clear_screen.blit(self.target, (hov.getCenter()[0] - 16, hov.getCenter()[1] - 16))
        # We also draw an info box on the map to show the player anything they may need to know about the current unit
        if self.unitQueue:
            self.drawUnitInfo()

    def drawInfo(self, hov):
        name = self.lrg_font.render(hov.getName(), True, self.c["black"], self.c["light_grey"])
        name_rect = name.get_rect()
        name_rect.left = self.infoRect.left + 5
        name_rect.top = self.infoRect.top + 7.5
        self.screen.blit(name, name_rect)
        rect = pygame.Rect(self.infoRect.left, self.infoRect.top + 40, self.infoRect.width, 35)
        if type(hov) == location.Territory:
            # We show who the territory belongs to by giving their color
            col_border = pygame.Rect(self.infoRect.right - 65, name_rect.top, 60, 32.5)
            pygame.draw.rect(self.screen, self.c["black"], col_border)
            col_box = pygame.Rect(col_border.left + 5, col_border.top + 5, col_border.width - 10,
                                  col_border.height - 10)
            if hov.getOwner():
                pygame.draw.rect(self.screen, hov.getOwner().getColor(), col_box)
            else:
                pygame.draw.rect(self.screen, [255, 255, 255], col_box)
            self.drawResources(self.resourceNames, hov.getResources(), rect)
            rect.top = rect.bottom
            self.drawStats([r'\power', r'\defense', r'\aquatic', r'\arial'],
                           [hov.attPower(), hov.defPower(), hov.getCoast().navPower(), hov.ariPower()], rect)
            self.drawResources(self.resourceNames, self.pc.getResources(), self.resourceRect)
        else:
            self.drawResources(self.resourceNames, hov.getCost(), rect)
            rect.top = rect.bottom
            self.drawStats(hov.getAttributes(), hov.getValues(), rect)
            self.drawResources(self.resourceNames, self.pc.getResources(), self.resourceRect)

    def drawUnitInfo(self):
        unit_drawn = self.unitQueue[0]

        has_capacity = unit_drawn.isAquatic() or type(unit_drawn) == unit.Helicopter

        if has_capacity:
            unit_info = pygame.Rect(30, self.height - 165, 220, 135)
        else:
            unit_info = pygame.Rect(30, self.height - 115, 220, 85)
        pygame.draw.rect(self.screen, self.c["black"], unit_info)
        unit_info = pygame.Rect(unit_info.left + 5, unit_info.top + 5, unit_info.width - 10, unit_info.height - 10)
        pygame.draw.rect(self.screen, self.c["light_grey"], unit_info)
        unit_circ = pygame.draw.circle(self.screen, self.c["black"], (unit_info.left + 20, unit_info.top + 20), 18)
        unit_drawn.draw(self.screen, unit_circ.center)
        if type(unit_drawn) == unit.AircraftCarrier:
            font = self.sml_font
        else:
            font = self.med_font
        name_box = font.render(unit_drawn.getName(), True, self.c["black"], self.c["light_grey"])
        name_rect = name_box.get_rect()
        name_rect.centery = unit_circ.centery
        name_rect.left = unit_circ.right + 5
        self.screen.blit(name_box, name_rect)
        stats = pygame.Rect((unit_info.left, unit_info.top + 45), (unit_info.width, 35))
        self.drawStats(unit_drawn.getAttributes(), unit_drawn.getValues(), stats)
        if has_capacity:
            pygame.draw.line(self.screen, self.c["black"],
                             (stats.left + 10, stats.centery + 15), (stats.right - 10, stats.centery + 15))
            x, y = unit_info.left + 20, unit_info.bottom - 20

            for brd in unit_drawn.getBoarded():
                brd.draw(self.screen, (x, y))
                x += 15

    # Redraws the shop to show any Boarding units
    def drawBoarding(self):
        choices = []
        pygame.draw.rect(self.screen, self.c["black"], self.shopRect)
        ship_rect = pygame.Rect(self.shopRect.left + 5, self.shopRect.top + 5, self.shopRect.width - 10, 50)
        for ship in self.boardableUnits:
            choices.append(pygame.Rect(ship_rect.left, ship_rect.top, ship_rect.width, ship_rect.height))
            pygame.draw.rect(self.screen, self.c["light_grey"], ship_rect)

            img = pygame.transform.scale(pygame.image.load(r'.\images' + data.unit_info[ship.getName()] + r'.png'), (50, 50))
            self.screen.blit(img, ship_rect)

            if ship.isAquatic() or type(ship) == unit.Helicopter:
                cap_img = pygame.transform.scale(pygame.image.load(r'.\images\capacity.png'), (20, 20))
                self.screen.blit(cap_img, (ship_rect.left + 50, ship_rect.top + 5))

                cap = ship.getCapacity()
                cap_txt = self.sml_font.render(str(cap), True, self.c["black"], self.c["light_grey"])
                self.screen.blit(cap_txt, (ship_rect.left + 75, ship_rect.top + 5))

                arw = pygame.Rect(ship_rect.left + 50, ship_rect.top + 34, 35, 8)
                pygame.draw.rect(self.screen, self.c["black"], arw)
                arw_head = [(arw.right, arw.top - 4), (arw.right + 15, arw.centery - 1), (arw.right, arw.bottom + 4)]
                pygame.draw.polygon(self.screen, self.c["black"], arw_head)

                x, y = ship_rect.left + 125, ship_rect.centery
                for un in ship.getBoarded():
                    un.draw(self.screen, (x, y))
                    x += 15

                ship_rect.top = ship_rect.bottom + 5
        return choices

    # Called within a while loop, updates the game state and visual state for the user
    def update(self, player_num, msg=None):
        # The return value for the update function. This is not None when some significant occurs during the game tick
        ret_val = None

        # This parses your opponents turns! Anything they do will be run here :)
        if msg is not None:
            self.parseMessage(msg)

        # Get the position of our mouse for this frame
        x, y = pygame.mouse.get_pos()

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

    # OPPONENTS
    # -----------------------------------------------------------------------------------

    def parseMessage(self, msg):
        # Start Game Function
        if msg[0] == 0:
            self.startGame(self.players[msg[1]], self.territories[msg[2]])
        # Purchase Function
        elif msg[0] == 1:
            self.purchaseUnit(self.players[msg[1]], self.territories[msg[2]], self.units[msg[3]])
        # Move Function
        elif msg[0] == 2:
            self.move(self.players[msg[1]], self.territories[msg[2]], self.players[msg[1]].getUnits()[msg[3]])
        elif msg[0] == 3:
            self.attack(self.players[msg[1]], self.territories[msg[2]], self.players[msg[1]].getUnits()[msg[3]])
        elif msg[0] == 4:
            self.arialAttack(self.players[msg[1]], self.territories[msg[2]], self.players[msg[1]].getUnits()[msg[3]])
        elif msg[0] == 5:
            self.embark(self.players[msg[1]], self.players[msg[1]].getUnits()[msg[2]], self.players[msg[1]].getUnits()[msg[3]])
        elif msg[0] == 6:
            self.disembark(self.players[msg[1]], self.players[msg[1]].getUnits()[msg[2]], self.players[msg[1]].getUnits()[msg[3]])
"""