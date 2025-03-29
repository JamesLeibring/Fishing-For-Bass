# Fishin Fer Bass
import controller
import server

if __name__ == "__main__":
  # Enter your name and send to the server
  pcName = input('\nWelcome to Fishing For Bass!\n\nEnter your name: ')

  # Create the client
  client = server.Client()

  # Send the players name
  client.send(pcName)

  print('\nWaiting for other players to connect. Fishing should open in just a moment!')

  # Receive the names of the players
  names = client.recv().split(',')

  FishingForBass = controller.Controller(names, pcName)

  FishingForBass.startGame()

  while FishingForBass.gameLoop():
    FishingForBass.draw()
  
  # Close the connection with the server
  client.close()
