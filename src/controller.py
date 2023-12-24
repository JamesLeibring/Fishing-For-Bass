from classes import ConfigPygame
import pygame

import drawer

import player, location, unit

class Controller:
    def __init__(self, playerNames, pc):
        self.config = ConfigPygame()

        # The Drawer draws everything we need on the screen
        self.drawer = drawer.Drawer()

        # The Players for this game
        self.players = [player.Player(i, playerNames[i]) for i in range(len(playerNames))]
        self.pc = self.players[pc]

        # The territories for this game
        # self.territories = [location.Territory(ter) for ter in self.config['Territories']]
        # self.coasts = [location.Coast(coast) for coast in self.config['Locations']['Coasts']]

        # The different units to be used (these are only used to project info)
        self.units = [unit.makeUnit(name, self.pc) for name in self.config['Units'] if name == 'Warrior' ]

        # The turn the game is on
        self.turn = 0

        # The item the users mouse is hovering over
        self.hov = None

    def gameLoop(self):
        self.drawer.drawBackground(self.pc.playerNum)

        # Boolean for when the game is running
        running = True

        while running:
            # Get the position of our mouse for this frame
            self.hov = self.hover(pygame.mouse.get_pos())

            self.drawer.draw(self.turn, self.pc, self.hov, len(self.players))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # Hover function determines if you are hovering a unit or territory and returns it
    def hover(self, loc):
        x = loc[0]
        y = loc[1]

        for ply in self.players:
            if ply.inside(x, y):
                return ply
        #for ter in self.territories:
        #    if ter.inside(x, y):
        #        return ter
        for un in self.units:
            if un.inside(x, y):
                return un

        return None