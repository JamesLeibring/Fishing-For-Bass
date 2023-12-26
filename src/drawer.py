from classes import ConfigPygame

import pygame

import player, location, unit

class Drawer:
  def __init__(self, config:ConfigPygame) -> None:
    # Config Information
    self.config = config

    # Start up pygame
    pygame.init()

    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    self.screen = pygame.display.set_mode(self.config.gettuple('SCREEN', 'width_height'))

    # The surface is used as a way to print opaque objects
    self.surface = pygame.Surface(self.config.gettuple('SCREEN', 'width_height'), pygame.SRCALPHA)

  # Draws a rectangle given a name
  def drawRect(self, rect:pygame.Rect, color:pygame.Color, border:int) -> None:
    pygame.draw.rect(self.screen, self.config.getcolor('black'), rect)

    rect = pygame.Rect(rect.left + border, rect.top + border, rect.width - border*2, rect.height - border*2)

    return pygame.draw.rect(self.screen, color, rect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self) -> None:
    # Caption the game
    pygame.display.set_caption('Fishing For Bass')

    # Fill the screen
    self.screen.fill(self.config.getcolor('burntsienna'))

    objects = ['MAP', 'SIDEBAR', 'TURN', 'COLOR', 'RESOURCE', 'SHOP', 'INFO']

    for obj in objects:
      rect = self.config.getrect(obj)
      color = self.config.getcolor(self.config.get(obj, 'color'))
      border = self.config.getint(obj, 'border')

      self.drawRect(rect, color, border)
  
    pygame.display.flip()

  # Draws the player icons
  def drawMap(self, players:list[player.Player]) -> None:
    for plyr in players:
      self.drawRect(plyr.rect, plyr.color, 5)


  # Draw the game state
  def drawSide(self) -> None:
    pygame.display.flip()