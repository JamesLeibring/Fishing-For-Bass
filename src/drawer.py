import pygame
import config as config_

class Drawer:
  def __init__(self):
    # Config Information
    self.config = config_.config['Drawer']

    # Start up pygame
    pygame.init()

    # Create our initial screens, the first is normal, the second has the ability to create opaque objects
    self.screen = pygame.display.set_mode((self.config['Screen']['width'], self.config['Screen']['height']))
    self.screen.fill(self.config['Colors']['burntsienna'])

    pygame.display.set_caption('Fishing For Bass')

    # The surface is used as a way to print opaque objects
    self.surface = pygame.Surface((self.config['Surface']['width'], self.config['Surface']['height']), pygame.SRCALPHA)

    # Fonts to be used in drawings
    self.fonts = {
      'lrg': pygame.font.Font('freesansbold.ttf', 33),
      'med': pygame.font.Font('freesansbold.ttf', 25),
      'sml': pygame.font.Font('freesansbold.ttf', 15)
    }

    # A dictionary of images
    self.images = {}

    # The map and target images
    self.makeImage(self.config['Images']['Map']),

    # The Unit and Resource Images
    self.makeImages(self.config['Images']['Units'])
    self.makeImages(self.config['Images']['Resources'])
  
  # Creates an image to be drawn
  def makeImage(self, info):
    self.images[info['name']] = pygame.transform.scale(pygame.image.load(info['image']), (info['width'], info['height']))

  # Createa a set of images to be drawn
  def makeImages(self, info):
    for name in info['name']:
      self.images[name] = pygame.transform.scale(pygame.image.load(info['name'][name]), (info['width'], info['height']))

  def drawRect(self, info):
    return pygame.draw.rect(self.screen, self.config['Colors'][info['color']], (info['start'][0], info['start'][1], info['width'], info['height']))
  
  def drawBorder(self, outer, color, border):
    return pygame.draw.rect(self.screen, self.config['Colors'][color], (outer.left + border, outer.top + border, outer.width - 2*border, outer.height - 2*border))
  
  def drawText(self, text, size, rect, align='center'):
    t = self.fonts[size].render(text, True, self.config['Colors']['black'], self.config['Colors']['cornsilk'])
    tRect = t.get_rect()
    
    if align == 'center':
      tRect.center = rect.center
    elif align == 'left':
      tRect.midleft = rect.midleft
    
    self.screen.blit(t, tRect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self, playerNum):
    # Draw the border
    self.borderRect = self.drawRect(self.config['Rects']['Border'])

    # Draw the map
    self.mapRect = self.drawRect(self.config['Rects']['Map'])

    # Draw the sidebar
    self.sideRect = self.drawRect(self.config['Rects']['Side'])

    # Draw the info box
    self.infoRect = self.drawRect(self.config['Rects']['Info'])
    self.drawBorder(self.infoRect, 'cornsilk', 5)

    # Draw the turn box
    self.turnRect = self.drawRect(self.config['Rects']['Turn'])
    self.drawBorder(self.turnRect, 'cornsilk', 5)

    # Draw the color box (indicates which player you are)
    self.colorRect = self.drawRect(self.config['Rects']['Color'])
    self.drawBorder(self.colorRect, self.config['Colors']['Player'][playerNum], 5)

    # Draw the resources box
    self.resourceRect = self.drawRect(self.config['Rects']['Resources'])
    self.drawBorder(self.resourceRect, 'cornsilk', 5)

    # Draw the shop border
    self.shopRect = self.drawRect(self.config['Rects']['Shop'])
    self.drawBorder(self.shopRect, 'white', 5)

  # Draws the Map
  def drawMap(self, playerNum):
    self.screen.blit(self.images['Map'], self.drawBorder(self.mapRect, 'white', 0))

    info = self.config['Rects']['PlayerBoxes']

    for i in range(playerNum):
      rect = self.drawRect(info[i+1])
      self.drawBorder(rect, self.config['Colors']['Player'][i], 5)

  # Draw the shop
  def drawShop(self, playerNum, selectedUnit=None):
    self.drawBorder(self.shopRect, 'cornsilk2', 5)

    for name in self.config['Rects']['ShopBoxes']:
      rect = self.drawRect(self.config['Rects']['ShopBoxes'][name])

      if name == selectedUnit:
        color = 'cornsilk'
      else:
        color = self.config['Colors']['Player'][playerNum]

      self.screen.blit(self.images[name], self.drawBorder(rect, color, 5))
  
  # Draw the turn
  def drawTurn(self, turn):
    rect = self.drawBorder(self.turnRect, 'cornsilk', 5)
    self.drawText('Turn: ' + str(turn), 'lrg', rect)

  # Draw the resource values at the top of the screen
  def drawResources(self, resources):
    rect = self.drawBorder(self.resourceRect, 'cornsilk', 5)
    imgs = [self.images['Food'], self.images['Wood'], self.images['Metal'], self.images['Oil']]

    self.drawStats(imgs, resources, rect)

  # Draws the info box
  def drawInfo(self, info=None):
    rect = self.drawBorder(self.infoRect, 'cornsilk', 5)

    if info is not None:   
      name = info[0]
      color = self.config['Colors']['Player'][info[1] - 1]
      resources = info[2]
      images = [self.images[img] for img in info[3]]

      # Draw the name
      self.drawText(name, 'med', pygame.Rect(rect.left + 10, rect.top + 5, rect.width / 2 - 5, rect.height / 2 - 5), 'left')

      # Draw the color of the owner
      colorRect = pygame.draw.rect(self.screen, self.config['Colors']['black'], (rect.right - 50, rect.top + 10, 40, 40))
      self.drawBorder(colorRect, color, 5)

      # The divider
      pygame.draw.line(self.screen, self.config['Colors']['black'], (rect.left + 5, rect.centery), (rect.right - 5, rect.centery), 3)

      # The resources
      self.drawStats(images, resources, pygame.Rect(rect.left, rect.top + 65, rect.width, rect.height))

  # Draws 4 stats
  def drawStats(self, imgs, values, rect):
    left = rect.left
    top = rect.top

    for i in range(4):
      self.screen.blit(imgs[i], (left, top))

      left += self.config['Images']['Resources']['width']

      self.drawText(str(values[i]), 'sml', pygame.Rect(left, top, 25, self.config['Images']['Resources']['height']))

      left += 25

  # Flip the screen to the current drawn status
  def flip(self):
    pygame.display.flip()