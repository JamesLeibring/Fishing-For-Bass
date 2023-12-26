from configparser import ConfigParser, ExtendedInterpolation
import pygame

import player, location, unit

# An extension from the config parser object
class ConfigPygame(ConfigParser):
  def __init__(self) -> None:
    super().__init__(interpolation=ExtendedInterpolation())

  # Returns a pygame surface (image) from the config
  def getimage(self, image:str, size:int) -> pygame.Surface:
    url = self.get('IMAGES', image)

    return pygame.transform.scale(pygame.image.load(url), (size, size))

  # Returns a pygame Color object from the config
  def getcolor(self, color:str) -> pygame.Color:
    rgb = self.gettuple('COLORS', color)

    return pygame.Color(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) == 4 else 255)
  
  # Returns a pygame Font object from the config
  def getfont(self, size:str) -> pygame.font.Font:
    font = self.get('FONTS', 'font')
    size = self.getint('FONTS', size)

    return pygame.font.Font(font, size)
  
  # Returns a pygame rectangle from the config
  def getrect(self, rect:str) -> pygame.Rect:
    topleft = self.gettuple(rect, 'topleft')
    bottomright = self.gettuple(rect, 'bottomright')

    return self.parserect(topleft, bottomright)
  
  # Returns a player object from the config
  def getplayer(self, number:int, name:str) -> player.Player:
    data = self.getdict('PLAYERS', str(number))

    color = self.getcolor(data['color'])
    rect = self.parserect(data['topleft'], data['bottomright'])

    return player.Player(name, number, color, rect)
  
  # Returns a tuple object from the config
  def gettuple(self, section:str, option:str) -> tuple:
    # The tuple to be parsed
    string = self.get(section, option)

    # Return a tuple split and converted to int when possible
    return self.parsetuple(string)

  # Returns a list object from the config
  def getlist(self, section:str, option:str) -> list:
    # If the string was not given, find it amongst the options
    string = self.get(section, option)

    # Return a list split and converted to tuples when possible
    return self.parselist(string)

  # Returns a dict object from the config  
  def getdict(self, section:str, option:str) -> dict:
    # If the string was not given, find it amongst the options
    string = self.get(section, option)

    # Return a dictionary split and converted to lists/tuples/ints when possible
    return self.parsedict(string)
  
  # Returns a rectangle given a topleft and bottomright
  def parserect(self, topleft:tuple[int,int], bottomright:tuple[int,int]) -> pygame.Rect:
    width_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])

    return pygame.Rect(topleft, width_height)

  # Parses a string into a tuple
  def parsetuple(self, string:str) -> tuple:
    return tuple(self.parse(x) for x in string[1:-1].split('.'))

  # Parse a string into a list
  def parselist(self, string:str) -> list:
    return list(self.parse(x) for x in string[1:-1].split('|'))

  # Parse a string into a dict
  def parsedict(self, string:str) -> dict:
    return dict(self.parse(x) for x in string.split(','))
  
  # Parse a key value pair into key and value
  def parsepair(self, string:str) -> tuple:
    return tuple(self.parse(x) for x in string.split(':'))

  # Parse a value into its proper type
  def parse(self, string:str):
    # Strip white space from the start and end of a string
    string = string.strip()

    if string.startswith('[') and string.endswith(']'):
      return self.parselist(string)
    
    if string.startswith('(') and string.endswith(')'):
      return self.parsetuple(string)
    
    if ':' in string:
      return self.parsepair(string)

    return int(string) if string.isdigit() else string