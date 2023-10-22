import pygame

class Drawer:
  def __init__(self, config):
    # Information about the main screen
    self.screenInfo = config['Screen']

    # Information about the main surface
    self.surfaceInfo = config['Surface']

    # Color information
    self.colors = config['Colors']

    # Image information
    self.imageInfo = config['Images']

    # Rectangle Dimension Information
    self.rectInfo = config['Rects']

    # Start up pygame
    pygame.init()

    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    self.screen = pygame.display.set_mode((self.screenInfo['width'], self.screenInfo['height']))
    self.screen.fill(self.colors['fill'])

    pygame.display.set_caption('Fishing For Bass')

    # The surface is used as a way to print opaque objects
    self.surface = pygame.Surface((self.surfaceInfo['width'], self.surfaceInfo['height']), pygame.SRCALPHA)

    # Fonts to be used in drawings
    self.fonts = {
      'lrg': pygame.font.Font('freesansbold.ttf', 35),
      'med': pygame.font.Font('freesansbold.ttf', 25),
      'sml': pygame.font.Font('freesansbold.ttf', 20)
    }

    # Images to be drawn in later
    self.mapImage = self.makeImage(self.imageInfo['Map'])
    self.targetImage = self.makeImage(self.imageInfo['Target'])
  
  # Creates an image to be drawn
  def makeImage(self, info):
    image = pygame.image.load(info['name'])
    return pygame.transform.scale(image, (info['width'], info['height']))
  
  # Create a rectangle to be drawn
  def makeRect(self, info):
    return pygame.draw.rect(self.screen, self.colors[info['color']], (info['start'][0], info['start'][1], info['width'], info['height']))
  
  # Creates a border for a given rectangle
  def makeBorder(self, outer, color, border):
    pygame.draw.rect(self.screen, self.colors[color], (outer.left + border, outer.top + border, outer.width - 2*border, outer.height - 2*border))

  def drawBackground(self, playerColor):
    # Draw the border
    self.borderRect = self.makeRect(self.rectInfo['Border'])

    # Draw the map
    self.mapRect = self.makeRect(self.rectInfo['Map'])

    # Draw the sidebar
    self.sideRect = self.makeRect(self.rectInfo['Side'])

    # Draw the info box
    self.infoRect = self.makeRect(self.rectInfo['Info'])
    self.makeBorder(self.infoRect, 'light_grey', 5)

    # Draw the turn box
    self.turnRect = self.makeRect(self.rectInfo['Turn'])
    self.makeBorder(self.turnRect, 'light_grey', 5)

    # Draw the color box (indicates which player you are)
    self.colorRect = self.makeRect(self.rectInfo['Color'])
    self.makeBorder(self.colorRect, playerColor, 5)

    # Draw the resources box
    self.resourceRect = self.makeRect(self.rectInfo['Resources'])
    self.makeBorder(self.resourceRect, 'light_grey', 5)

    # Draw the shop border
    self.shopRect = self.makeRect(self.rectInfo['Shop'])
    self.makeBorder(self.shopRect, 'red', 5)
  
  def draw(self):
    pygame.display.flip()