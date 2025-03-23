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
    self.fonts:dict[str, pygame.font.Font] = {size: Config._font(size) for size in config.FONTS if size != 'font'}

    # Rectangle Data
    self.rects:dict[str, Rect] = {rect: Config._rect(rect) for rect in config.RECTANGLES}

    # Player Data
    self.players:list[Player] = [Player(name) for name in players]

    # Unit Data
    self.units:list[Unit] = [
      Warrior(True), Horseman(True), Swordsman(True), Knight(True),
      Musketman(True), Cavalry(True), Infantry(True), Tank(True),
      Archer(True), Cannon(True), Artillery(True), AntiAirGun(True),
      Trireme(True), Caravel(True), Battleship(True), AircraftCarrier(True),
      Fighter(True), Bomber(True), JetFighter(True), Helicopter(True)
    ]

    # Territory Data
    self.territories:dict[str, Territory] = {ter: Config._territory(ter) for ter in config.TERRITORIES}

  # Returns a pygame surface (image) from the config
  def _image(name:str) -> pygame.Surface:
    image = config.IMAGES[name]

    file = image['image']
    size = image['dimensions']

    return pygame.transform.scale(pygame.image.load(file), size)

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

  def copy(self:Rect) -> Rect:
    return Rect(self.border, self.color, (self.border.w - self.rect.h) / 2)

  def move(self:Rect, x:int, y:int) -> None:
    self.border = self.border.move(x, y)
    self.rect = self.rect.move(x, y)

class Player:

  ID = 0

  # The location of the unplayer boxt
  LOCATION:Rect = Config._rect('player')

  # Player Colors
  COLORS:pygame.Color = [
    Config._color('skyblue'),
    Config._color('cobaltgreen'),
    Config._color('firebrick'),
    Config._color('darkorange'),
    Config._color('yellow'),
    Config._color('gray')
  ]

  def __init__(self:Player, name:str) -> None:
    # The unique player id for this player. Then increment ID's
    self.id = Player.ID
    Player.ID += 1

    # The Players Name
    self.name = name

    # The player box for this player (when hovered, updates info box)
    self.rect = Player.LOCATION.copy()
    self.rect.move(45 * self.id, 0)

    self.rect.color = Player.COLORS[self.id]

    # The territories and costs owned by the player
    self.territories:list[Territory] = []

    # Player resources
    self.food = 0
    self.wood = 0
    self.metal = 0
    self.oil = 0

    # Player per turn resources
    self.food_per = 0
    self.wood_per = 0
    self.metal_per = 0
    self.oil_per = 0

    self.power = 0

  # Returns a list of stats for the player
  def stats(self:Player) -> list[int]:
    return [self.food, self.wood, self.metal, self.oil]
  
  # Returns a list of stats per turn for the player
  def stats_per_turn(self:Player) -> list[int]:
    return [self.food_per, self.wood_per, self.metal_per, self.oil_per]

  # Determines if the mouse is hovering this player object
  def inside(self:Player, mouse:tuple[int]) -> bool:
    return self.rect.rect.collidepoint(mouse[0], mouse[1])

# The Location Class
class Territory:
  def __init__(self:Territory, name:str, rect:Rect, border:list[tuple[int]], yields:tuple[int]) -> None:
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
  def stats(self:Territory) -> list[int]:
    return [self.food, self.wood, self.metal, self.oil, self.power]

  # Determines if the mouse is hovering this territory object
  def inside(self:Territory, mouse:tuple[int]) -> bool:
    return self.rect.rect.collidepoint(mouse[0], mouse[1])

class Unit:

  ID = 0

  # The location of the unit
  LOCATION:Rect = Config._rect('unit')

  def __init__(self:Unit, name:str, defensive:bool=False) -> None:
    # The unique unit id for this unit and increment ID's
    self.id = Unit.ID
    Unit.ID += 1

    self.name = name

    # The image and location associated with the unit
    self.image:pygame.Surface = Config._image(name)
    self.rect = Unit.LOCATION.copy()

    if not defensive:
      self.power = config.UNITS[name]['power']
    else:
      self.power = config.UNITS[name]['defense']

    self.movement = config.UNITS[name]['movement']

    self.defensive = defensive
    self.special = None

  # Determines if the mouse is hovering this unit object
  def inside(self:Unit, mouse:tuple[int,int]) -> bool:
    return self.rect.rect.collidepoint(mouse[0], mouse[1])

  # Moves the unit to the center of a given rectangle
  def move(self:Unit, rect:Rect) -> None:
    self.rect.rect.center = rect.rect.center

  # Returns a list of the stats to display
  def stat_names(self:Unit) -> list[str]:
    return ['power' if not self.defensive else 'defense', 'movement']

  # Returns a list of stats for the unit
  def stats(self:Unit) -> list[int]:
    return [self.power, self.movement]

class Ship(Unit):
  def __init__(self:Ship, name:str, defensive:bool=False) -> None:
    super().__init__(name, defensive)

    self.capacity = config.UNITS[name]['capacity']
  
  def stat_names(self:Ship) -> list[str]:
    return ['naval' if not self.defensive else 'aquadef', 'movement', 'capacity']
  
  def stats(self:Ship) -> list[int]:
    return super().stats() + [self.capacity]

class Plane(Unit):
  def __init__(self:Plane, name:str, defensive:bool=False) -> None:
    super().__init__(name, defensive)

    self.range = config.UNITS[name]['range']

  def stat_names(self:Plane) -> list[str]:
    return ['arial', 'movement', 'range']

  def stats(self:Plane) -> list[int]:
    return super().stats() + [self.range]

class Warrior(Unit):
  def __init__(self:Warrior, shop:bool=False) -> None:
    super().__init__('warrior')

    if shop: self.rect.move(1180, 190)

class Horseman(Unit):
  def __init__(self:Horseman, shop:bool=False) -> None:
    super().__init__('horseman')

    if shop: self.rect.move(1245, 190)

class Swordsman(Unit):
  def __init__(self:Swordsman, shop:bool=False) -> None:
    super().__init__('swordsman')

    if shop: self.rect.move(1335, 190)

class Knight(Unit):
  def __init__(self:Knight, shop:bool=False) -> None:
    super().__init__('knight')

    if shop: self.rect.move(1400, 190)

class Musketman(Unit):
  def __init__(self:Musketman, shop:bool=False) -> None:
    super().__init__('musketman')

    if shop: self.rect.move(1180, 270)

class Cavalry(Unit):
  def __init__(self:Cavalry, shop:bool=False) -> None:
    super().__init__('cavalry')

    if shop: self.rect.move(1245, 270)

class Infantry(Unit):
  def __init__(self:Infantry, shop:bool=False) -> None:
    super().__init__('infantry')

    if shop: self.rect.move(1335, 270)

class Tank(Unit):
  def __init__(self:Tank, shop:bool=False) -> None:
    super().__init__('tank')

    if shop: self.rect.move(1400, 270)

class Archer(Unit):
  def __init__(self:Archer, shop:bool=False) -> None:
    super().__init__('archer', defensive=True)

    if shop: self.rect.move(1180, 350)

class Cannon(Unit):
  def __init__(self:Cannon, shop:bool=False) -> None:
    super().__init__('cannon', defensive=True)

    if shop: self.rect.move(1245, 350)

class Artillery(Unit):
  def __init__(self:Artillery, shop:bool=False) -> None:
    super().__init__('artillery', defensive=True)

    if shop: self.rect.move(1335, 350)

class AntiAirGun(Unit):
  def __init__(self:AntiAirGun, shop:bool=False) -> None:
    super().__init__('anti-air_gun', defensive=True)

    if shop: self.rect.move(1400, 350)

    # Special Ability: Anti-Air
    self.special = 'anti-air'

  def stat_names(self:AntiAirGun) -> list[str]:
    return super().stat_names() + [self.special]
  
  def stats(self:AntiAirGun) -> list[int]:
    return super().stats() + [-1]

class Trireme(Ship):
  def __init__(self:Trireme, shop:bool=False):
    super().__init__('trireme', defensive=True)

    if shop: self.rect.move(1180, 430)

class Caravel(Ship):
  def __init__(self:Caravel, shop:bool=False):
    super().__init__('caravel')

    if shop: self.rect.move(1245, 430)

class Battleship(Ship):
  def __init__(self:Battleship, shop:bool=False) -> None:
    super().__init__('battleship')

    if shop: self.rect.move(1335, 430)

class AircraftCarrier(Ship):
  def __init__(self:AircraftCarrier, shop:bool=False):
    super().__init__('aircraft_carrier', defensive=True)

    if shop: self.rect.move(1400, 430)

    # Special Ability: Anti-Air
    self.special = 'carrier'

  def stat_names(self:AntiAirGun) -> list[str]:
    return super().stat_names() + [self.special]
  
  def stats(self:AntiAirGun) -> list[int]:
    return super().stats() + [-1]

class Fighter(Plane):
  def __init__(self:Fighter, shop:bool=False) -> None:
    super().__init__('fighter')

    if shop: self.rect.move(1180, 510)

class Bomber(Plane):
  def __init__(self:Bomber, shop:bool=False) -> None:
    super().__init__('bomber')

    if shop: self.rect.move(1245, 510)

class JetFighter(Plane):
  def __init__(self:JetFighter, shop:bool=False) -> None:
    super().__init__('jet_fighter')

    if shop: self.rect.move(1335, 510)

class Helicopter(Plane):
  def __init__(self:Helicopter, shop:bool=False) -> None:
    super().__init__('helicopter')

    if shop: self.rect.move(1400, 510)

    # Special Ability: Anti-Air
    self.special = 'airlift'
    self.capacity = config.UNITS['helicopter']['capacity']

  def stat_names(self:AntiAirGun) -> list[str]:
    return super().stat_names() + [self.special]
  
  def stats(self:AntiAirGun) -> list[int]:
    return super().stats() + [self.capacity]
