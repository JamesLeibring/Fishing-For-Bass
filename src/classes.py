from __future__ import annotations

import pygame, config

# Helper for pulling back end data
class Config:
  # Transform all config inputs to usable obects
  def __init__(self:Config, players:list[str]) -> None:
    # Screen Data
    self.screen = config.SCREEN['dimensions']
    self.fill = config.SCREEN['color']

    # Image Data
    self.images:dict[str, pygame.Surface] = {image: Config._image(image) for image in config.IMAGES}

    # Color Data
    self.colors:dict[str, pygame.Color] = {color: Config._color(color) for color in config.COLORS}

    # Font Data
    self.fonts:dict[str, pygame.font.Font] = {size: Config._font(size) for size in config.FONTS if size is not 'font'}

    # Rectangle Data
    self.rects:dict[str, Rect] = {rect: Config._rect(rect) for rect in config.RECTANGLES}

    # Player Data
    self.players:dict[str, Player] = {plyr: Config._player(plyr, players[plyr]) for plyr in range(len(config.PLAYERS))}

    # Unit Data
    self.units:dict[str, Unit] = {un: Config._unit(un) for un in config.UNITS}

    # Territory Data
    self.territories:dict[str, Territory] = {ter: Config._territory(ter) for ter in config.TERRITORIES}

  # Returns a pygame surface (image) from the config
  def _image(image:str) -> pygame.Surface:
    url = config.IMAGES[image]

    return pygame.image.load(url)

  # Returns a pygame Color object from the config
  def _color(color:str) -> pygame.Color:
    rgb = config.COLORS[color]
  
    return pygame.Color(rgb[0], rgb[1], rgb[2], rgb[3] if len(rgb) == 4 else 255)
  
  # Returns a pygame Font object from the config
  def _font(size:str) -> pygame.font.Font:
    font = config.FONTS['font']
    size = config.FONTS[size]

    return pygame.font.Font(font, size)

  # Returns a pygame rectangle from the config
  def _rect(name:str) -> Rect:
    rectangle = config.RECTANGLES[name]

    topleft = rectangle['topleft']
    bottomright = rectangle['bottomright']

    length_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])
    return Rect(pygame.Rect(topleft, length_height), Config._color(rectangle['color']), rectangle['border'])

  # Returns a player object from the config
  def _player(number:int, name:str) -> Player:
    plyr = config.PLAYERS[number]

    topleft = plyr['topleft']
    bottomright = plyr['bottomright']

    length_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])
    rect = Rect(pygame.Rect(topleft, length_height), Config._color(plyr['color']), plyr['border'])

    return Player(name, number, rect)
  
  # Returns a unit object from the config
  def _unit(name:str) -> Unit:
    un = config.UNITS[name]

    topleft = un['topleft']
    bottomright = un['bottomright']

    length_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])
    rect = Rect(pygame.Rect(topleft, length_height), Config._color(un['color']), un['border'])

    return Unit(name, 0, rect, Config._image(name))

  # Returns a territory object from the config
  def _territory(name:str) -> Territory:
    ter = config.TERRITORIES[name]

    topleft = ter['topleft']
    bottomright = ter['bottomright']

    length_height = (bottomright[0] - topleft[0], bottomright[1] - topleft[1])
    rect = Rect(pygame.Rect(topleft, length_height), Config._color(ter['color']), 0)

    return Territory(name, rect, ter['land'], ter['yields'])

class Rect:
  def __init__(self:Rect, rect:pygame.Rect, color:pygame.Color, border:int) -> None:
    self.border = rect
    self.rect = pygame.Rect(rect.move(border, border).topleft, (rect.w - border*2, rect.h - border*2))

    self.color = color

class Player:
  def __init__(self, name:str, number:int, rect:Rect) -> None:
    # The Players Name
    self.name = name

    # The order within the turn the player goes
    self.number = number

    # The player box for this player (when hovered, updates info box)
    self.rect = rect

    # The territories and costs owned by the player
    self.territories:list[Territory] = []

    # Player resources
    self.food = 0
    self.wood = 0
    self.metal = 0
    self.oil = 0

    self.power = 0

  # Returns a list of stats for the player
  def stats(self) -> list[int]:
    return [self.food, self.wood, self.metal, self.oil]

  # Determines if the mouse is hovering this player object
  def inside(self, mouse:tuple[int]) -> bool:
    return self.rect.rect.collidepoint(mouse[0], mouse[1])

# The Location Class
class Territory:
  def __init__(self, name:str, rect:Rect, border:list[tuple[int]], yields:tuple[int]) -> None:
    # The name of the territory
    self.name = name

    # The border for the territory
    self.border = border

    # A rectangle for determining when the territory is selected
    self.rect = rect

    # Territory resources
    self.food = yields[0]
    self.wood = yields[1]
    self.metal = yields[2]
    self.oil = yields[3]

    self.power = 0

  # Returns a list of stats for the territory
  def stats(self) -> list[int]:
    return [self.food, self.wood, self.metal, self.oil, self.power]

  # Determines if the mouse is hovering this territory object
  def inside(self, mouse:tuple[int]) -> bool:
    return self.rect.rect.collidepoint(mouse[0], mouse[1])

class Unit:
  def __init__(self, name:str, id_:int, rect:Rect, image:pygame.Surface):
    # The name of this unit
    self.name = name

    # The unique unit id for this unit
    self.id = id_

    # The shop box for this unit (when hovered, updates info box)
    self.rect = rect

    # The image associated with the unit
    self.image = image

  # Determines if the mouse is hovering this unit object
  def inside(self, mouse:tuple[int,int]) -> bool:
    return self.rect.rect.collidepoint(mouse[0], mouse[1])

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
