import pygame

class Drawer:
  def __init__(self, config):
    self.width, self.height = str(config['width']), str(config['height'])

    # Start up pygame
    pygame.init()

    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    screen = pygame.display.set_mode((config['width'], config['height']))
    clear_screen = pygame.Surface((width - 360, height - 20), pygame.SRCALPHA)
    pygame.display.set_caption('Fishing For Bass')