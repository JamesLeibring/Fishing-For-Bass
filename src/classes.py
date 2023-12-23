import configparser, logging, pygame

# A config object is simply an object that uses values from the config
class ConfigObject:
  def __init__(self, config:configparser.ConfigParser) -> None:
    # The actual config object
    self.config = config

  # Returns a pygame surface of the image requested
  def image(self, image:str) -> pygame.Surface:
    url = self.config['IMAGES'][image]

    size = self.config.getint('IMAGES', 'size')

    return pygame.transform.scale(pygame.image.load(url), (size, size))

  # Returns a pygame Color object given a color to retrieve
  def color(self, color:str) -> pygame.Color:
    rgb = self.gettuple('COLORS', color)

    return pygame.Color(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) == 4 else 255)
  
  # Returns a pygame rectangle given name
  def rect(self, rect:str) -> pygame.Rect:
    topleft = self.gettuple(rect, 'topleft')
    bottomright = self.gettuple(rect, 'bottomright')

    width_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])

    return pygame.Rect(topleft, width_height)

  # Parses a string in form '1-9' into an int
  def getint(self, section:str, option:str) -> int:
    return self.config.getint(section, option)

  # Parses a string in form 'x.y' into a tuple of form (x, y)
  def gettuple(self, section:str, option:str) -> tuple:
    return tuple(int(x) for x in self.config[section][option].split('.'))