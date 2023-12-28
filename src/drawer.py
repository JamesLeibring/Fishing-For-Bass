from classes import ConfigPygame

import pygame

import player, territory, unit

import string

# Custom types
type GameObject = player.Player | territory.Territory | unit.Unit
type Coord = tuple[int]

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
    self.background['info']['iconrect'] = self.config.parserect(self.background['info']['icontopleft'], self.background['info']['iconbottomright'])

  # Draws a rectangle given a name
  def drawRect(self, rect:pygame.Rect, color:pygame.Color, border:int) -> None:
    pygame.draw.rect(self.screen, self.config.getcolor('black'), rect)

    rect = pygame.Rect(rect.move(border, border).topleft, (rect.w - border*2, rect.h - border*2))

    pygame.draw.rect(self.screen, color, rect)
  
  # Draws text in the given spot
  def drawText(self, text:str, size:str, coordinates:tuple[int], alignment:str='left') -> None:
    # Format the text
    text = string.capwords(text.replace('_', ' '))

    # Render the text
    format_text = self.config.getfont(size).render(text, 0, self.config.getcolor('black'))

    # Frame the text
    rect = format_text.get_rect()

    # Align the rendered text
    match alignment:
      case 'left':
        rect.midleft = coordinates
      case 'middle':
        rect.center = coordinates
      case 'right':
        rect.midright = coordinates

    # Draw the text on the screen
    self.screen.blit(format_text, rect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self) -> None:
    # Caption the game
    pygame.display.set_caption('Fishing For Bass')

    # Fill the screen
    self.screen.fill(self.config.getcolor('burntsienna'))

    for item in self.background.values():
      self.drawRect(item['rect'], item['color'], item['border'])

    pygame.display.flip()
  
  # Draws a 
  def drawResources(self, stats:list[int], rect:pygame.Rect):
    pass

  # Draws the player icons
  def draw(self, players:list[player.Player], units:list[unit.Unit], hov:GameObject|None, turn:int) -> None:        
    info:dict = self.background['info']
    inforect:pygame.Rect = info['rect']
    iconrect:pygame.Rect = info['iconrect']

    # Draw the turn
    self.drawText('Turn ' + str(turn), 'lrg', self.background['turn']['rect'].center, 'middle')

    match type(hov):
      case player.Player:
        # Draw the icon
        self.drawRect(iconrect, hov.color, 5)

        # Draw the name
        self.drawText(hov.name, 'med', iconrect.move(50,0).midleft, 'left')

        # Draws the divider line
        pygame.draw.line(self.screen, self.config.getcolor('black'), inforect.move(10,0).midleft, inforect.move(-10,0).midright, 5)

        # Highlight each territory the player owns
        for ter in hov.territories:
          pygame.draw.polygon(self.surface, ter.color, ter.border)
        
        #Draw the surface atop the screen
        self.screen.blit(self.surface, (0,0))

      case territory.Territory:
        # Draw the icon
        self.drawRect(iconrect, hov.color, 5)

        # Draw the name
        self.drawText(hov.name, 'med', iconrect.move(50,0).midleft, 'left')

        # Draws the divider line
        pygame.draw.line(self.screen, self.config.getcolor('black'), inforect.move(10,0).midleft, inforect.move(-10,0).midright, 5)

        # Highlight the selected territory
        pygame.draw.polygon(self.surface, hov.color, hov.border)
    
        # Draw the surface atop the screen
        self.screen.blit(self.surface, (0,0))

      case unit.Unit:
        # Draw the icon
        self.drawRect(iconrect, hov.color, 5)
        self.screen.blit(pygame.transform.scale(hov.image, (iconrect.w, iconrect.h)), iconrect)

        # Draws the divider line
        pygame.draw.line(self.screen, self.config.getcolor('black'), inforect.move(10,0).midleft, inforect.move(-10,0).midright, 5)

      case _:
        # Clears the surface for the next frame
        self.surface.fill([0,0,0,0])

        # Redraws the map of the game
        self.screen.blit(self.map, self.maprect)

        # Redraw the player boxes
        for plyr in players:
          self.drawRect(plyr.rect, plyr.color, plyr.border)
    
        # Redraws the units in the shop
        for un in units:
          self.drawRect(un.rect, un.color, un.border)
          self.screen.blit(un.image, un.rect)

        # Redraw the info box to clear the slate
        self.drawRect(inforect, info['color'], info['border'])

    pygame.display.flip()