# The Player Class: This holds all information for the player
import pygame

class Player:
  def __init__(self, name:str, number:int, color:pygame.Color, rect:pygame.Rect) -> None:
    # The Players Name
    self.name = name

    # The order within the turn the player goes
    self.number = number

    # The color associated with the player
    self.color = color

    # The player box for this player (when hovered, updates info box)
    self.rect = rect

    # The territories and costs owned by the player
    self.territories = []
    self.coasts = []

    # Player resources
    self.food = 0
    self.wood = 0
    self.metal = 0
    self.oil = 0
  
  # Returns a list of stats for the player
  def stats(self) -> list[int]:
    return [self.food, self.wood, self.metal, self.oil]
  
  # Determines if the mouse is hovering this player object
  def inside(self, mouse:tuple[int,int]) -> bool:
    return self.rect.collidepoint(mouse[0], mouse[1])