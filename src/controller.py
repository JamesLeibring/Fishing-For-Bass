from classes import ConfigPygame, configparser

import pygame, drawer
import player, location, unit

class Controller:
  def __init__(self, playerNames:set[str], pcName:str) -> None:
    # The config object
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # A special config object that reads and converts to pygame objects
    self.config = ConfigPygame(config)

    # The amount of players in the game
    self.playerNum = len(playerNames)

    # The Drawer draws everything needed on the screen
    self.drawer = drawer.Drawer(self.config)

    # The players in the game
    self.players = [self.config.getplayer(playerNames[i], i) for i in range(self.playerNum)]
    self.pc = [plyr for plyr in self.players if plyr.name == pcName][0]

    # The turn the game is on
    self.turn = 0

    # The item the users mouse is hovering over
    self.hov = None

  # Get the game ready for play
  def startGame(self) -> None:
    self.drawer.drawBackground()

  def gameLoop(self) -> bool:
    # Get the position of our mouse for this frame
    self.hov = self.hover(pygame.mouse.get_pos())

    for event in pygame.event.get():
      match event.type:
        case pygame.QUIT:
          return False
    
    return True

  # Hover function determines if you are hovering a unit or territory and returns it
  def hover(self, loc:tuple[int,int]) -> tuple[int,int]:
    x, y = loc[0], loc[1]

    return (x, y)