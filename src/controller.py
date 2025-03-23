from __future__ import annotations

import pygame, drawer

from classes import Config, Player, Territory, Unit

type GameObject = Player | Territory | Unit

class Controller:
  def __init__(self:Controller, playerNames:list[str], pcName:str) -> None:
    # Start up pygame
    pygame.init()

    # The config object
    self.config = Config(playerNames)

    self.players = self.config.players
    self.territories = self.config.territories
    self.units = self.config.units

    # Set the player character
    self.pc = self.players[playerNames.index(pcName)]
    self.config.rects['color'].color = self.pc.rect.color

    # The Drawer draws everything needed on the screen
    self.drawer = drawer.Drawer(self.config)

    # The item the users mouse is hovering over
    self.hov = None
    self.turn = 0
    self.player_turn = 0

  # Get the game ready for play
  def startGame(self:Controller) -> None:
    self.drawer.drawBackground(self.pc.name)

  def gameLoop(self:Controller):
    # Get the position of our mouse for this frame
    self.hov = self.hover(pygame.mouse.get_pos())

    # Tests all events that occured this frame
    for event in pygame.event.get():
      match event.type:
        case pygame.QUIT:
          return False
    
    return True
    
  # Hover function determines if you are hovering a unit or territory and returns it
  def hover(self:Controller, mouse:tuple[int,int]) -> GameObject | None:
    # Determine if the mouse is hovering over a player
    for player in self.players:
      if player.inside(mouse):
        return player

    # Determine if the mouse is hovering over a territory
    for ter in self.territories.values():
      if ter.inside(mouse):
        return ter

    # Determine if the mouse is hovering over a unit in the shop
    for unit in self.units:
      if unit.inside(mouse):
        return unit

    return None
  
  # Draw the screen
  def draw(self:Controller) -> None:
    self.drawer.draw(self.players, self.pc, self.hov, self.turn, self.player_turn)