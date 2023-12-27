from classes import ConfigPygame

import pygame, drawer
import player, territory, unit

class Controller:
  def __init__(self, playerNames:list[str], pcName:str) -> None:
    # The config object
    self.config = ConfigPygame()
    self.config.read('config.ini')

    # The players in the game
    self.players = [self.config.getplayer(i, name) for i, name in enumerate(playerNames)]
    self.pc = self.players[playerNames.index(pcName)]

    # The territories in the game

    # The units in the game
    self.units = [self.config.getunit(0, name) for name in self.config['UNITS']]

    # The Drawer draws everything needed on the screen
    self.drawer = drawer.Drawer(self.config, self.pc)

    # The turn the game is on
    self.turn = 0

    # The item the users mouse is hovering over
    self.hov = None

  # Get the game ready for play
  def startGame(self) -> None:
    self.drawer.drawBackground(self.pc)

  def gameLoop(self):
    # Get the position of our mouse for this frame
    self.hov = self.hover(pygame.mouse.get_pos())

    # Tests all events that occured this frame
    for event in pygame.event.get():
      match event.type:
        case pygame.QUIT:
          return False
    
    return True
    
  # Hover function determines if you are hovering a unit or territory and returns it
  def hover(self, mouse:tuple[int,int]) -> player.Player | unit.Unit | None:
    # Determine if the mouse is hovering over a player
    for player in self.players:
      if player.inside(mouse):
        return player
    
    # Determine if the mouse is hovering over a unit
    for unit in self.units:
      if unit.inside(mouse):
        return unit

    return None
  
  # Draw the screen
  def draw(self) -> None:
    self.drawer.drawMap(self.players)

    self.drawer.drawSide(self.units, self.hov)