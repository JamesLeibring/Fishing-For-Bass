# The Player Class: This holds all information for the player

class Player:
  def __init__(self, name, number, color) -> None:
    # The Players Name
    self.name = name

    # The order within the turn the player goes
    self.number = number

    # The color associated with the player
    self.color = color

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