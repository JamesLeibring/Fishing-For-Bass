# Fishin Fer Bass
import controller
import server
import threading

from time import sleep

def host_server(players:int) -> None:
  server.Server(players)

if __name__ == "__main__":
  # Begin the server if this is the host machine
  host = input('\nWelcome to Fishing For Bass!\n\nAre you the host of this game? (y/n): ')

  if host == 'y':
    playerCount = int(input('Including you, how many players are in your game? (1-6): '))

    threading.Thread(target=host_server, args=[playerCount]).start()

  sleep(0.5)

  # Enter your name and send to the server
  pcName = input('Enter your name: ')
  print()

  # Create the client
  client = server.Client()

  # Send the players name
  client.send(pcName)

  print('\nWaiting for other players to connect. Fishing should open in just a moment!')

  # Receive the names of the players
  names = client.recv().split(',')

  print('\nAll players connected! Opening Fishing For Bass now!\n')

  FishingForBass = controller.Controller(names, pcName)

  FishingForBass.startGame()

  while FishingForBass.gameLoop():
    FishingForBass.draw()
  
  # Close the connection with the server
  client.close()
