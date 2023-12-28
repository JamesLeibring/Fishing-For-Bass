import pygame

import territory

class Player:
  def __init__(self, name:str, number:int, rect:pygame.Rect, color:pygame.Color, border:int) -> None:
    # The Players Name
    self.name = name

    # The order within the turn the player goes
    self.number = number

    # The player box for this player (when hovered, updates info box)
    self.rect = rect

    # The color associated with the player
    self.color = color

    # The border for the rect of the player object
    self.border = border

    # The territories and costs owned by the player
    self.territories:list[territory.Territory] = []

    # Player resources
    self.food = 0
    self.wood = 0
    self.metal = 0
    self.oil = 0

    self.power = 0
  
  # Returns a list of stats for the player
  def stats(self) -> list[int]:
    return [self.food, self.wood, self.metal, self.oil, self.power]
  
  # Determines if the mouse is hovering this player object
  def inside(self, mouse:tuple[int]) -> bool:
    return self.rect.collidepoint(mouse[0], mouse[1])