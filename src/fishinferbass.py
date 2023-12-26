# Fishin Fer Bass
import controller, time

if __name__ == "__main__":
  names = ['Tyler', 'Matt', 'James', 'Zack', 'Tedsta', 'Dopeguy13']
  myname = 'James'

  FishingForBass = controller.Controller(names, myname)

  FishingForBass.startGame()

  while FishingForBass.gameLoop():
    FishingForBass.draw()