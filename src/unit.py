# The Unit Class : Describes a unit in its entirity
import config
import pygame

class Unit:
  def __init__(self, name:str, id:int, rect:pygame.Rect, color:pygame.Color, image:pygame.Surface, border:int):
    # The name of this unit
    self.name = name
    # The unique unit id for this unit
    self.id = id

    # The shop box for this unit (when hovered, updates info box)
    self.rect = rect

    # The color associated with the unit
    self.color = color

    # The image associated with the unit
    self.image = image

    # The border size for the shop box unit
    self.border = border

  # Determines if the mouse is hovering this unit object
  def inside(self, mouse:tuple[int,int]) -> bool:
    return self.rect.collidepoint(mouse[0], mouse[1])