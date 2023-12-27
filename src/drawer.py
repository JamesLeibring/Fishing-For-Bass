from classes import ConfigPygame

import pygame

import player, territory, unit

import string

class Drawer:
  def __init__(self, config:ConfigPygame, pc:player.Player) -> None:
    # Config Information
    self.config = config

    # Start up pygame
    pygame.init()

    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    self.screen = pygame.display.set_mode(self.config.gettuple('SCREEN', 'width_height'))

    # The surface is used as a way to print opaque objects
    self.surface = pygame.Surface(self.config.gettuple('SCREEN', 'width_height'), pygame.SRCALPHA)

    # The rectangle the map lies on
    self.maprect = self.config.parserect(config.gettuple('MAP', 'topleft'), config.gettuple('MAP', 'bottomright'))

    # The image of the map itself
    self.map = self.config.getimage('map', self.maprect.w, self.maprect.h)   

    # The information for drawing the information box
    self.background = dict((name, self.config.getdict('BACKGROUND', name)) for name in self.config['BACKGROUND'])

    # Configuring settings
    for item in self.background.values():
      item['color'] = self.config.getcolor(item['color'])
      item['rect'] = self.config.parserect(item['topleft'], item['bottomright'])

    # Custom settings
    self.background['color']['color'] = pc.color

  # Draws a rectangle given a name
  def drawRect(self, rect:pygame.Rect, color:pygame.Color, border:int) -> None:
    pygame.draw.rect(self.screen, self.config.getcolor('black'), rect)

    rect = pygame.Rect(rect.left + border, rect.top + border, rect.w - border*2, rect.h - border*2)

    pygame.draw.rect(self.screen, color, rect)
  
  # Draws text in the given spot
  def drawText(self, text:str, size:str, midright:tuple[int,int]) -> None:
    words = self.config.getfont(size).render(text, 0, self.config.getcolor('black'))

    rect = words.get_rect()
    rect.midright = midright

    self.screen.blit(words, rect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self, pc:player.Player) -> None:
    # Caption the game
    pygame.display.set_caption('Fishing For Bass')

    # Fill the screen
    self.screen.fill(self.config.getcolor('burntsienna'))

    for item in self.background.values():
      self.drawRect(item['rect'], item['color'], item['border'])

    pygame.display.flip()

  # Draws the player icons
  def drawMap(self, players:list[player.Player]) -> None:
    # Draws the map of the game
    self.screen.blit(self.map, self.maprect)

    for plyr in players:
      # Draws the player box on the map
      self.drawRect(plyr.rect, plyr.color, plyr.border)

    pygame.display.flip()

  # Draw the sideboard
  def drawSide(self, units:list[unit.Unit], hov:player.Player|unit.Unit|None) -> None:
    for un in units:
      # Draws the unit shop box for the shop
      self.drawRect(un.rect, un.color, un.border)
      # Draws the image of the unit for each box
      self.screen.blit(un.image, un.rect)
    
    info = self.background['info']

    # Draws the info box as a background
    self.drawRect(info['rect'], info['color'], info['border'])

    # Draw the info box if something is being hovered
    if hov is not None: self.drawInfo(hov, info)

  # Draw the info box
  def drawInfo(self, hov:player.Player|territory.Territory|unit.Unit, info:dict) -> None:
    # The rects for the info box
    rect = info['rect']
    icon = self.config.parserect(info['icontopleft'], info['iconbottomright'])

    # Draws the divider line
    pygame.draw.line(self.screen, self.config.getcolor('black'), (rect.left + 10, rect.centery), (rect.right - 10, rect.centery), 5)

    # Draw the name
    self.drawText(string.capwords(hov.name.replace('_', ' ')), 'med', (rect.right - 10, icon.centery))

    match type(hov):
      case player.Player:
        # Draw the icon
        self.drawRect(icon, hov.color, hov.border)
      case territory.Territory:
        # Draw the territory icon
        self.drawRect(icon, hov.color, 5)
      case unit.Unit:
        # Draw the icon
        self.drawRect(icon, hov.color, hov.border)

        # Draw the unit image
        self.screen.blit(pygame.transform.scale(hov.image, (icon.w, icon.h)), icon)
  
    pygame.display.flip() 