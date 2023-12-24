from classes import ConfigPygame

from player import Player

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
    self.images = self.makeImages()
  
  # Createa a set of images to be drawn
  def makeImages(self):
    imgDict = {}

    for imgName in self.config['Images']:
      info = self.config['Images'][imgName]

      if type(info['image']) == str:
        imgDict[imgName] = pygame.transform.scale(pygame.image.load(info['image']), (info['width'], info['height']))
      else:
        for img in info['image']:
          imgDict[img] = pygame.transform.scale(pygame.image.load(info['image'][img]), (info['width'], info['height']))
    
    return imgDict

  def drawRect(self, info):
    return pygame.draw.rect(self.screen, self.config['Colors'][info['color']], (info['start'][0], info['start'][1], info['width'], info['height']))
  
  def drawBorder(self, outer, color, border):
    return pygame.draw.rect(self.screen, self.config['Colors'][color], (outer.left + border, outer.top + border, outer.width - 2*border, outer.height - 2*border))
  
  def drawText(self, text, size, rect, left=False):
    t = self.fonts[size].render(text, True, self.config['Colors']['black'], self.config['Colors']['cornsilk'])
    tRect = t.get_rect()
    
    if left:
      tRect.midleft = rect.midleft
    else:
      tRect.center = rect.center
    
    self.screen.blit(t, tRect)

  # Draws the background for the game (1 time draw)
  def drawBackground(self, playerNum):
    # Draw the border
    self.borderRect = self.drawRect(self.config['Dimensions']['Border'])

    # Draw the map
    self.mapRect = self.drawRect(self.config['Dimensions']['Map'])

    # Draw the sidebar
    self.sideRect = self.drawRect(self.config['Dimensions']['Side'])

    # Draw the info box
    self.infoRect = self.drawRect(self.config['Dimensions']['Info'])
    self.drawBorder(self.infoRect, 'cornsilk', 5)

    # Draw the turn box
    self.turnRect = self.drawRect(self.config['Dimensions']['Turn'])
    self.drawBorder(self.turnRect, 'cornsilk', 5)

    # Draw the color box (indicates which player you are)
    self.colorRect = self.drawRect(self.config['Dimensions']['Color'])
    self.drawBorder(self.colorRect, self.config['Colors']['Player'][playerNum], 5)

    # Draw the resources box
    self.resourceRect = self.drawRect(self.config['Dimensions']['Resources'])
    self.drawBorder(self.resourceRect, 'cornsilk', 5)

    # Draw the shop border
    self.shopRect = self.drawRect(self.config['Dimensions']['Shop'])
    self.drawBorder(self.shopRect, 'white', 5)

  # Draws the Map
  def drawMap(self, playerNum):
    self.screen.blit(self.images['Map'], self.drawBorder(self.mapRect, 'white', 0))

    for i in range(playerNum):
      rect = self.drawRect(self.config['Dimensions']['PlayerBoxes'][i])
      self.drawBorder(rect, self.config['Colors']['Player'][i], 5)

  # Draw the shop
  def drawShop(self, playerNum, selectedUnit=None):
    self.drawBorder(self.shopRect, 'cornsilk2', 5)

    for name in self.config['Dimensions']['ShopBoxes']:
      rect = self.drawRect(self.config['Dimensions']['ShopBoxes'][name])

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
  def drawResources(self, stats):
    rect = self.drawBorder(self.resourceRect, 'cornsilk', 5)
    self.drawStats(stats, rect)

  # Draws the info box
  def drawInfo(self, x):
    rect = self.drawBorder(self.infoRect, 'cornsilk', 5)

    if x is None: return

    # Draw the name
    self.drawText(x.name, 'med', pygame.Rect(rect.left + 10, rect.top + 5, rect.width / 2 - 5, rect.height / 2 - 5), left=True)

    # Find the color to draw in the top right
    if type(x) == Player:  
      playerNum = x.playerNum
    else:
      playerNum = x.player.playerNum

    color = self.config['Colors']['Player'][playerNum]

    # Draw the color of the owner
    colorRect = pygame.draw.rect(self.screen, self.config['Colors']['black'], (rect.right - 50, rect.top + 10, 40, 40))
    self.drawBorder(colorRect, color, 5)
    
    # The divider
    pygame.draw.line(self.screen, self.config['Colors']['black'], (rect.left + 5, rect.centery), (rect.right - 5, rect.centery), 3)

    # The resources
    self.drawStats(x.stats, pygame.Rect(rect.left, rect.top + 65, rect.width, rect.height))

  # Draws 4 stats
  def drawStats(self, stats, rect):
    # Create a new Rect to draw our shapes
    rect = pygame.Rect(rect.left, rect.top, 50, 50)
    
    # Loop through each stat, drawing it
    for stat in stats:
      # Format the image
      img = self.images[stat]
      imgRect = img.get_rect()
      imgRect.center = rect.center

      self.screen.blit(img, imgRect)

      rect.left += 50

      # Format the text
      text = str(stats[stat])
      if len(text) < 3:
        size = 'med'
      else:
        size = 'sml'

      self.drawText(text, size, pygame.Rect(rect.left, rect.top, 25, 50))

      rect.left += 25

  # Draw the game state
  def draw(self, turn, player, hov, playerCount):
    # Draw the turn label
    self.drawTurn(turn)

    # Draw the resource bar
    self.drawResources(player.stats)

    # Draw the shop
    self.drawShop(player.playerNum)

    # Draw the info box
    self.drawInfo(hov)

    # Draw the map
    self.drawMap(playerCount)

    pygame.display.flip()