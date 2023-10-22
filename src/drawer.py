import pygame

class Drawer:
  def __init__(self, config):
    # Information about the main screen
    self.screenInfo = config['Screen']

    # Information about the main surface
    self.surfaceInfo = config['Surface']

    # Color information
    self.colorInfo = config['Colors']

    # Image information
    self.imageInfo = config['Images']

    # Rectangle Dimension Information
    self.rectInfo = config['Rects']

    # Start up pygame
    pygame.init()

    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    self.screen = pygame.display.set_mode((self.screenInfo['width'], self.screenInfo['height']))
    self.screen.fill(self.colorInfo['burntsienna'])

    pygame.display.set_caption('Fishing For Bass')

    # The surface is used as a way to print opaque objects
    self.surface = pygame.Surface((self.surfaceInfo['width'], self.surfaceInfo['height']), pygame.SRCALPHA)

    # Fonts to be used in drawings
    self.fonts = {
      'lrg': pygame.font.Font('freesansbold.ttf', 35),
      'med': pygame.font.Font('freesansbold.ttf', 30),
      'sml': pygame.font.Font('freesansbold.ttf', 20)
    }

    # A dictionary of images
    self.images = {}

    # The map and target images
    self.makeImage(self.imageInfo['Map']),

    # The Unit and Resource Images
    self.makeImages(self.imageInfo['Units'])
    self.makeImages(self.imageInfo['Resources'])
  
  # Creates an image to be drawn
  def makeImage(self, info):
    self.images[info['name']] = pygame.transform.scale(pygame.image.load(info['image']), (info['width'], info['height']))

  # Createa a set of images to be drawn
  def makeImages(self, info):
    for name in info['name']:
      self.images[name] = pygame.transform.scale(pygame.image.load(info['name'][name]), (info['width'], info['height']))

  def drawRect(self, info):
    return pygame.draw.rect(self.screen, self.colorInfo[info['color']], (info['start'][0], info['start'][1], info['width'], info['height']))
  
  def drawBorder(self, outer, color, border):
    return pygame.draw.rect(self.screen, self.colorInfo[color], (outer.left + border, outer.top + border, outer.width - 2*border, outer.height - 2*border))
  
  def drawText(self, text, size, rect):
    t = self.fonts[size].render(text, True, self.colorInfo['black'], self.colorInfo['cornsilk'])
    tRect = t.get_rect()
    tRect.center = rect.center
    self.screen.blit(t, tRect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self, playerNum):
    # Draw the border
    self.borderRect = self.drawRect(self.rectInfo['Border'])

    # Draw the map
    self.mapRect = self.drawRect(self.rectInfo['Map'])

    # Draw the sidebar
    self.sideRect = self.drawRect(self.rectInfo['Side'])

    # Draw the info box
    self.infoRect = self.drawRect(self.rectInfo['Info'])
    self.drawBorder(self.infoRect, 'cornsilk', 5)

    # Draw the turn box
    self.turnRect = self.drawRect(self.rectInfo['Turn'])
    self.drawBorder(self.turnRect, 'cornsilk', 5)

    # Draw the color box (indicates which player you are)
    self.colorRect = self.drawRect(self.rectInfo['Color'])
    self.drawBorder(self.colorRect, self.colorInfo['Player'][playerNum], 5)

    # Draw the resources box
    self.resourceRect = self.drawRect(self.rectInfo['Resources'])
    self.drawBorder(self.resourceRect, 'cornsilk', 5)

    # Draw the shop border
    self.shopRect = self.drawRect(self.rectInfo['Shop'])
    self.drawBorder(self.shopRect, 'white', 5)

  # Draws the Map
  def drawMap(self, playerNum):
    self.screen.blit(self.images['Map'], self.drawBorder(self.mapRect, 'white', 0))

    info = self.rectInfo['PlayerBoxes']

    for i in range(playerNum):
      rect = self.drawRect(info)
      self.drawBorder(rect, self.colorInfo['Player'][i], 5)

      info['start'][0] += 45

  # Draw the shop
  def drawShop(self, playerNum, selectedUnit=None):
      self.drawBorder(self.shopRect, 'cornsilk2', 5)

      info = self.rectInfo['ShopBoxes']

      for i, name in enumerate(self.imageInfo['Units']['name']):
        unitRect = self.drawRect(info)

        if name == selectedUnit:
          color = 'cornsilk'
        else:
          color = self.colorInfo['Player'][playerNum]

        self.screen.blit(self.images[name], self.drawBorder(unitRect, color, 5))

        if (i+1) % 4 == 0:
          info['start'][0] = 1175
          
          if (i+1) % 12 == 0 or (i+1) % 16 == 0:
            info['start'][1] += 90
          else:
            info['start'][1] += 70

        elif (i+1) % 2 == 0:
          info['start'][0] += 80
        else:
          info['start'][0] += 70
  
  # Draw the turn
  def drawTurn(self, turn):
    rect = self.drawBorder(self.turnRect, 'cornsilk', 5)
    self.drawText('Turn: ' + str(turn), 'med', rect)

  # Draw the resource values at the top of the screen
  def drawResources(self, resources):
    rect = self.drawBorder(self.resourceRect, 'cornsilk', 5)
    imgs = [self.images['Food'], self.images['Wood'], self.images['Metal'], self.images['Oil']]

    self.drawStats(imgs, resources, rect)

  # Draws the info box
  def drawTerritoryInfo(self, name, resources):
    rect = self.drawBorder(self.infoRect, 'cornsilk', 5)
    imgs = [self.images['Food'], self.images['Wood'], self.images['Metal'], self.images['Oil']] # TODO: Tmp

    self.drawStats(imgs, resources, rect)

  # Draws 4 stats
  def drawStats(self, imgs, values, rect):
    left = rect.left + 10
    top = rect.top + 5

    for i in range(4):
      self.screen.blit(imgs[i], (left, top))

      left += self.imageInfo['Resources']['width']

      self.drawText(str(values[i]), 'sml', pygame.Rect(left, top, 25, self.imageInfo['Resources']['height']))

      left += 30

  # Flip the screen to the current drawn status
  def flip(self):
    pygame.display.flip()