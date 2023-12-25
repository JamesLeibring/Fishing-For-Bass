from configparser import ConfigParser, ExtendedInterpolation
import pygame

import player, location, unit

# A config object is simply an object that uses values from the config
class ConfigPygame(ConfigParser):
  def __init__(self) -> None:
    super().__init__(interpolation=ExtendedInterpolation())

  # Returns a pygame surface of the image requested
  def getimage(self, image:str) -> pygame.Surface:
    url = self.get('IMAGES', image)

    size = self.getint('IMAGES', 'size')

    return pygame.transform.scale(pygame.image.load(url), (size, size))

  # Returns a pygame Color object given a color to retrieve
  def getcolor(self, color:str) -> pygame.Color:
    rgb = self.gettuple('COLORS', color)

    return pygame.Color(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) == 4 else 255)
  
  # Returns a pygame Font object given a font size
  def getfont(self, size:str) -> pygame.font.Font:
    return pygame.font.Font(self.get('FONTS', 'font'), self.getint('FONTS', size))
  
  # Returns a pygame rectangle given name
  def getrect(self, rect:str) -> pygame.Rect:
    topleft = self.gettuple(rect, 'topleft')
    bottomright = self.gettuple(rect, 'bottomright')

    width_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])

    return pygame.Rect(topleft, width_height)
  
  # Returns a player object from the information
  def getplayer(self, name:str, number:int) -> dict:
    data = self.getdict('PLAYERS', str(number))

    return player.Player(name, number, self.getcolor(data['color']))

  # Parses a string in form 'x.y' into a tuple of form (x, y)
  def gettuple(self, section:str, option:str) -> tuple:
    return tuple(int(x) for x in self.get(section, option).split('.'))

  # Parses a dictionary in form 'key:value, key:a|b|c|d, key:a.b'
  def getdict(self, section:str, option:str) -> dict:
    d = dict()

    pairs = self.get(section, option)[1:].split(',')

    for pair in pairs:
      key, value = pair.split(':')

      # Case of list
      if value.startswith('[') and value.endswith(']'):
        value = value[1:-1].split('|')

        for v in value:
          v = tuple(int(x) for x in v.split('.'))

      # Case of tuple
      elif value.startswith('(') and value.endswith(')'):
        value = tuple(int(x) if x.isdigit() else x for x in value[1:-1].split('.'))
      
      # Case of int/string
      else:
        value = int(value) if value.isdigit() else value

      d[key] = value
    
    return d