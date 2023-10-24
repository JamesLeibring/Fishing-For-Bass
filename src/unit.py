# The Unit Class : Describes a unit in its entirity
import config
import pygame

class Unit:
    def __init__(self, id, player):        
        self.buttonInfo = config.config['Buttons']['Units']

        self.statInfo = config.config['Units']

        # The name of the unit
        self.name = None

        # The units unique id
        self.id = id

        # The units stats
        self.stats = None

        # The button
        self.button = None
        
        # The player owner
        self.player = player
    
    def makeButton(self, name):
        return pygame.Rect(self.buttonInfo['start'][name][0], self.buttonInfo['start'][name][1], self.buttonInfo['width'], self.buttonInfo['height'])
    
    def inside(self, x, y):
        return self.button.collidepoint(x, y)

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

# Specific units start here

class Warrior(Unit):
    def __init__(self, id, player):
        super().__init__(id, player)

        self.name = 'Warrior'

        self.stats = self.statInfo['Warrior']

        self.power = self.stats['Power']
        self.movement = self.stats['Movement']

        self.button = self.makeButton(self.name)

def makeUnit(name, player):
    if name == 'Warrior':
        return Warrior(0, player)
    else:
        return None