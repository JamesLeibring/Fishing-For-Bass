# Fishin Fer Bass
import controller, time

if __name__ == "__main__":
  names = ['James', 'Tyler', 'Matt', 'Zack', 'Tedsta', 'Dopeguy13']

  FishingForBass = controller.Controller(names, 'James')

  FishingForBass.startGame()

  while FishingForBass.gameLoop():
    FishingForBass.drawer.draw()