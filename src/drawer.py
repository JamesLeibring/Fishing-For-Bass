from classes import ConfigPygame

import pygame

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
  def drawRect(self, name:str) -> None:
    rect = self.config.getrect(name)

    pygame.draw.rect(self.screen, self.config.getcolor('black'), rect)

    border = self.config.getint(name, 'border')

    rect = pygame.Rect(rect.left + border, rect.top + border, rect.width - border*2, rect.height - border*2)

    color = self.config.getcolor(self.config.get(name, 'color'))

    pygame.draw.rect(self.screen, color, rect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self) -> None:
    # Caption the game
    pygame.display.set_caption('Fishing For Bass')

    # Fill the screen
    self.screen.fill(self.config.getcolor('burntsienna'))

    # Draw the border
    self.drawRect('MAP')

    # Draw the sidebar
    self.drawRect('SIDEBAR')

    # Draw the turn box
    self.drawRect('TURNBOX')

    # Draw the color box
    self.drawRect('COLORBOX')

    # Draw the resource box
    self.drawRect('RESOURCEBOX')

    # Draw the shop background
    self.drawRect('SHOPBOX')

    # Draw the info box
    self.drawRect('INFOBOX')
  
    pygame.display.flip()
  
  # Draw the shop options
  def drawShop(self) -> None:
    rect = pygame.Rect(self.config.gettuple('SHOP', 'topleft'), (self.config.getint('SHOP', 'size'), self.config.getint('SHOP', 'size')))

    for i, unit in enumerate(self.config['UNITS']):
      pygame.draw.rect(self.screen, self.config.getcolor('black'), rect)

      self.screen.blit(self.config.getimage(unit), rect)

      if i + 1 % 4 == 0:
        rect.move(-200, 70)


  # Draw the game state
  def draw(self) -> None:
    self.drawShop()

    pygame.display.flip()