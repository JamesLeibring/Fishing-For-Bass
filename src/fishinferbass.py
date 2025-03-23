# Fishin Fer Bass
import controller
import time
if __name__ == "__main__":
  names = ['Tyler', 'Matt', 'James', 'Zack', 'Teddy', 'Rose']
  myname = 'James'

  FishingForBass = controller.Controller(names, myname)

  FishingForBass.startGame()

  while FishingForBass.gameLoop():
    FishingForBass.draw()