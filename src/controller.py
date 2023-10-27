import config
import drawer
import player
import location
import unit
import pygame

class Controller:
    def __init__(self, playerNames, pc):
        self.config = config.config

        # The buttons for the game
        self.buttonInfo = self.config['Buttons']

        # The Drawer draws everything we need on the screen
        self.drawer = drawer.Drawer()

        # The Players for this game
        self.players = [player.Player(i, playerNames[i]) for i in range(len(playerNames))]
        self.pc = pc

        # The territories for this game
        self.territories = [location.Territory(ter) for ter in self.config['Locations']['Territories']]
        # self.coasts = [location.Coast(coast) for coast in self.config['Locations']['Coasts']]

        # The different units to be used (these are only used to project info)
        self.units = [unit.makeUnit(un, self.players[self.pc]) for un in self.config['Units']]

        # The turn the game is on
        self.turn = 0

        # The item the users mouse is hovering over
        self.hov = None

    def gameLoop(self):
        self.drawer.drawBackground(self.pc)

        # Boolean for when the game is running
        running = True

        while running:
            # Get the position of our mouse for this frame
            self.hov = self.hover(pygame.mouse.get_pos())

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # Draw the game state
    def draw(self):
        # Draw the turn label
        self.drawer.drawTurn(self.turn)

        # Draw the resource bar
        self.drawer.drawResources(self.players[self.pc].stats)

        # Draw the shop
        self.drawer.drawShop(self.pc)

        # Draw the info box
        self.drawer.drawInfo(self.hov)

        # Draw the map
        self.drawer.drawMap(len(self.players))

        self.drawer.flip()

    # Hover function determines if you are hovering a unit or territory and returns it
    def hover(self, loc):
        x = loc[0]
        y = loc[1]

        for ply in self.players:
            if ply.inside(x, y):
                return ply
        for ter in self.territories:
            if ter.inside(x, y):
                return ter
        for un in self.units:
            if un.inside(x, y):
                return un

        return None