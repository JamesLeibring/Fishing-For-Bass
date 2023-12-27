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

    # The rectangle the map lies on
    self.maprect = config.parserect(config.gettuple('MAP', 'topleft'), config.gettuple('MAP', 'bottomright'))

    # The image of the map itself
    self.map = config.getimage('map', self.maprect.width, self.maprect.height)   

  # Draws a rectangle given a name
  def drawRect(self, rect:pygame.Rect, color:pygame.Color, border:int) -> None:
    pygame.draw.rect(self.screen, self.config.getcolor('black'), rect)

    rect = pygame.Rect(rect.left + border, rect.top + border, rect.width - border*2, rect.height - border*2)

    pygame.draw.rect(self.screen, color, rect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self, pc:player.Player) -> None:
    # Caption the game
    pygame.display.set_caption('Fishing For Bass')

    # Fill the screen
    self.screen.fill(self.config.getcolor('burntsienna'))

    for name in self.config['BACKGROUND']:
      obj = self.config.getdict('BACKGROUND', name)

      rect = self.config.parserect(obj['topleft'], obj['bottomright'])
      color = pc.color if name == 'color' else self.config.getcolor(obj['color'])
      border = obj['border']

      self.drawRect(rect, color, border)
  
    pygame.display.flip()

  # Draws the player icons
  def drawMap(self, players:list[player.Player]) -> None:
    # Draws the map of the game
    self.screen.blit(self.map, self.maprect)

    for plyr in players:
      # Draws the player box on the map
      self.drawRect(plyr.rect, plyr.color, plyr.border)

    pygame.display.flip()


  # Draw the game state
  def drawSide(self, units:list[unit.Unit], hov:player.Player|unit.Unit|None) -> None:
    for un in units:
      # Draws the unit shop box for the shop
      self.drawRect(un.rect, un.color, un.border)
      # Draws the image of the unit for each box
      self.screen.blit(un.image, un.rect)
    
    match type(hov):
      case player.Player:
        print(hov.name)
      case unit.Unit:
        print(hov.name)

    pygame.display.flip() 