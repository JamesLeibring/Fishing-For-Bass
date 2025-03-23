from __future__ import annotations

import pygame
import string

from classes import Config, Rect, Player, Territory, Unit

type GameObject = Player | Territory | Unit

class Drawer:

  def __init__(self:Drawer, config:Config) -> None:
    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    self.screen = pygame.display.set_mode(config.screen)

    # The surface is used as a way to print opaque objects
    self.surface = pygame.Surface(config.screen, pygame.SRCALPHA)

    # Color used to fill in the bakcground
    self.fill = config.colors[config.fill]

    self.images = config.images
    self.colors = config.colors
    self.fonts = config.fonts
    self.rects = config.rects

    self.resources = ['food', 'wood', 'metal', 'oil']

    self.shop = config.units

  # Draws the background for the game (1 time draw)
  def drawBackground(self:Drawer) -> None:
    # Caption the game
    pygame.display.set_caption('Fishing For Bass')

    # Fill the screen
    self.screen.fill(self.fill)

    background = ['map', 'gamebar', 'turn', 'color', 'resource', 'shop', 'info']

    for feature in background:
      self.drawRect(self.rects[feature])

    pygame.display.flip()

  # Draws a rectangle given rectangle, its color, and the width of the border
  def drawRect(self:Drawer, rect:Rect) -> None:
    pygame.draw.rect(self.screen, self.colors['black'], rect.border)
    pygame.draw.rect(self.screen, rect.color, rect.rect)
  
  # Draws text in the given spot
  def drawText(self:Drawer, text:str, size:str, rect:Rect, align_left:bool=False) -> None:
    # Format the text
    text = string.capwords(text.replace('_', ' '))

    # Render the text and center it on the rect given
    format_text = self.fonts[size].render(text, 0, self.colors['black'])
    text_rect = format_text.get_rect()

    if align_left:
      text_rect.midleft = rect.rect.midleft
    else:
      text_rect.center = rect.rect.center

    # Draw the text on the screen
    self.screen.blit(format_text, text_rect)
  
  # Draws a line of resources
  def drawResources(self:Drawer, resources:list[str], yields:list[int], rect:Rect):
    images = [self.images[resource] for resource in resources]

    rect = rect.copy()

    for stat, value in zip(images, yields):
      image_rect = stat.get_rect()
      image_rect.center = rect.rect.center
      
      # The image for the stat
      self.screen.blit(stat, image_rect)

      rect.move(37.5, 0)

      # The text for the stat
      if value >= 0:
        self.drawText(str(value), 'sml', rect)

      rect.move(37.5, 0) 

  # Draws the player icons
  def draw(self:Drawer, players:list[Player], pc:Player, hov:GameObject|None, turn:int) -> None:        
    # Draw the turn
    self.drawText('Turn ' + str(turn), 'lrg', self.rects['turn'])

    # Draw the player resources
    self.drawResources(self.resources, pc.stats(), self.rects['resource_stat'])

    match hov:
      case Player():
        # Draw the icon
        self.drawRect(self.rects['info'])

        # Draw the name and power symbol
        self.drawText(hov.name, 'med', self.rects['info_name'], align_left=True)
        self.drawResources(['power'], [hov.power], self.rects['info_power'])

        # Draws the divider line
        self.drawRect(self.rects['info_line'])

        # Draws the Per Turn Resources
        self.drawResources(self.resources, hov.stats_per_turn(), self.rects['info_stat'])

        # Highlight each territory the player owns
        for ter in hov.territories:
          pygame.draw.polygon(self.surface, ter.rect.color, ter.border)

        # Draw the surface atop the screen
        self.screen.blit(self.surface, (0,0))
      case Territory():
        # Draw the icon
        self.drawRect(self.rects['info'])

        # Draw the name and power symbol
        self.drawText(hov.name, 'med', self.rects['info_name'], align_left=True)
        self.drawResources(['power'], [hov.power], self.rects['info_power'])

        # Draws the divider line
        self.drawRect(self.rects['info_line'])

        # Draws the Per Turn Resources
        self.drawResources(self.resources, hov.stats(), self.rects['info_stat'])

        # Highlight the selected territory
        pygame.draw.polygon(self.surface, hov.rect.color, hov.border)

        # Draw the surface atop the screen
        self.screen.blit(self.surface, (0,0))
      case Unit():
        # Draw the icon
        self.drawRect(self.rects['info'])

        # Draw the name
        self.drawText(hov.name, 'med', self.rects['info_name'], align_left=True)

        # Draw the units image
        rect = hov.image.get_rect()
        rect.center = (self.rects['info_power'].rect.centerx + 20, self.rects['info_power'].rect.centery)
        self.screen.blit(hov.image, rect)

        # Draws the divider line
        self.drawRect(self.rects['info_line'])

        # Draws the Per Turn Resources
        self.drawResources(hov.stat_names(), hov.stats(), self.rects['info_stat'])

      case _:
        # Clears the surface for the next frame
        self.surface.fill(self.colors['clear'])

        # Redraws the map of the game
        self.screen.blit(self.images['map'], self.rects['map'])

        # Redraw the player boxes
        for plyr in players:
          self.drawRect(plyr.rect)
    
        # Redraws the units in the shop
        for item in self.shop:
          self.drawRect(item.rect)

          rect = item.image.get_rect()
          rect.center = item.rect.rect.center

          self.screen.blit(item.image, rect)

        # Redraw the info box to clear the slate
        self.drawRect(self.rects['info'])

    pygame.display.flip()

# Turn a integer into a Roman Numeral
def roman(number):
  ret_val = ""

  num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

  i = 12

  while number:
    div = number // num[i]
    number %= num[i]
  
    while div:
      ret_val += sym[i]
      div -= 1
  
    i -= 1
  return ret_val