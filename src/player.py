import pygame

import config as config_

class Player:
    def __init__(self, player, name):
        # Config Objects
        self.config = config_.config['Buttons']['Players']

        self.name = name

        # The player number    
        self.player = player

        # The territories and costs owned by the player
        self.territories = []
        self.coasts = []

        # The resources of the player
        self.resources = [0, 0, 0, 0]

        # The button for the player
        self.button = pygame.Rect(self.config['start'][self.player][0], self.config['start'][self.player][1], self.config['width'], self.config['height'])
    
    # Returns true if the point is on the button
    def inside(self, x, y):
        return self.button.collidepoint(x, y)
    
    # Returns information for when this is hoverd
    def info(self):
        return [self.name, self.player, self.resources, ['Food', 'Wood', 'Metal', 'Oil']]
