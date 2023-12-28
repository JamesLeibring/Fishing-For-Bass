import pygame

# The Location Class
class Territory:
  def __init__(self, name:str, border:list[tuple[int]], rect:pygame.Rect, color:pygame.Color, yields:tuple[int]) -> None:
    # The name of the territory
    self.name = name

    # The border for the territory
    self.border = border

    # A rectangle for determining when the territory is selected
    self.rect = rect

    # The color for the territory when highlighted
    self.color = color

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
    return self.rect.collidepoint(mouse[0], mouse[1])

# Turn a integer into a Roman Numeral
def roman(number):
  ret_val = ""
  num = [1, 4, 5, 9, 10, 40, 50, 90,
    100, 400, 500, 900, 1000]
  sym = ["I", "IV", "V", "IX", "X", "XL",
    "L", "XC", "C", "CD", "D", "CM", "M"]
  i = 12
  while number:
    div = number // num[i]
    number %= num[i]
    while div:
      ret_val += sym[i]
      div -= 1
    i -= 1
  return ret_val
