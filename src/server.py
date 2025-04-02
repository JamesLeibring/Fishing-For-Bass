from __future__ import annotations

import socket
import threading
import queue

THREAD_KILL = 'KILL'

class Server:

  HOST = '127.0.0.1'
  PORT = 34746

  def __init__(self:Server, num_connections:int) -> None:
    # Create the server socket and bind
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((Server.HOST, Server.PORT))

    print(f'\nServer started on {self.HOST}:{self.PORT}')

    # Queue of commands to broadcast to the clients
    self.commands_tx:list[queue.Queue[str]] = []
    self.commands_rx:queue.Queue[str] = queue.Queue()

    # The amount of active connections
    self.connections = 0

    # Character names
    names = ['UNKOWN'] * num_connections

    # Listen for X clients
    self.sock.listen(num_connections)

    for i in range(num_connections):
      print(f'Waiting for {num_connections - i} player(s) to connect...\n')

      # Accept a new client connection
      client_socket, client_address = self.sock.accept()
      self.connections += 1

      print(f'Connection made with Client at {client_address}')

      # Create a queue for commands sent to this socket
      client_queue:queue.Queue[str] = queue.Queue()
      self.commands_tx += [client_queue]

      # Create a new thread to handle the client connection
      threading.Thread(target=self.rx, args=(client_socket, client_address)).start()
      threading.Thread(target=self.tx, args=(client_socket, client_address, client_queue)).start()

      # Assign the characters name to the ID
      names[i] = self.commands_rx.get()
    
    # Once all connections are made, send the list of character names to the players
    self.queue_cmd(','.join(names))

  def rx(self:Server, sock:socket.socket, address:socket._RetAddress) -> None:
    # Listen to a client
    try:
      while True:
        # Receive message from the client
        message = sock.recv(1024).decode('utf-8')

        # Queue the command as received
        self.commands_rx.put(message)
    except ConnectionResetError:
      self.close_connection(sock, address)
    except ConnectionAbortedError:
      pass

  def tx(self:Server, sock:socket.socket, address:socket._RetAddress, queue:queue.Queue[str]) -> None:
    # Send commands to a client
    try:
      while True:
        # The next command to send
        cmd = queue.get()

        if cmd is THREAD_KILL:
          break

        # Send the command over the tcp connection
        sock.sendall(cmd.encode('utf-8'))
    except ConnectionResetError:
      self.close_connection(sock, address)

  def close_connection(self:Server, sock:socket.socket, address:socket._RetAddress) -> None:
    # Close down the connection to this socket
    sock.close()

    print(f'Connection closed with Client at {address}')

    if self.connections == 1:
      self.queue_cmd(THREAD_KILL)
      self.sock.close()

    self.connections -= 1

  def queue_cmd(self:Server, cmd:str) -> None:
    for q in self.commands_tx:
      q.put(cmd)


class Client:

  HOST = Server.HOST
  PORT = Server.PORT

  def __init__(self:Client) -> None:
    try:
      # Create the client socket and connect to host
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.connect((Client.HOST, Client.PORT))
    except ConnectionRefusedError:
      print(f'\nUnable to connect to Server')
      quit()
    else:
      print(f'Connection made with Server at {(Client.HOST, Client.PORT)}')

      self.commands_tx:queue.Queue[str] = queue.Queue()
      self.commands_rx:queue.Queue[str] = queue.Queue()

      # Start TX/RX communications
      threading.Thread(target=self.tx).start()
      threading.Thread(target=self.rx).start()

  def send(self:Client, cmd:str) -> None:
    self.commands_tx.put(cmd)

  def recv(self:Client) -> str:
    return self.commands_rx.get()

  def tx(self:Client) -> None:
    try:
      while True:
        # Prepare the command
        cmd = self.commands_tx.get()

        if cmd is THREAD_KILL:
          break

        # Send to the server
        self.sock.sendall(cmd.encode('utf-8'))
    except ConnectionResetError:
      print(f'Connection closed with Server at {(Client.HOST, Client.PORT)}')
      self.sock.shutdown(socket.SHUT_WR)

  def rx(self:Client) -> None:
    try:
      while True:
        # Receive command from server
        cmd = self.sock.recv(1024).decode('utf-8')

        # Queue the command recieved
        self.commands_rx.put(cmd)
    except ConnectionResetError:
      print(f'Connection closed with Server at {(Client.HOST, Client.PORT)}')
      self.sock.shutdown(socket.SHUT_RD)
    except ConnectionAbortedError:
      pass

  def close(self:Client) -> None:

    print(f'Connection closed with Server at {(Client.HOST, Client.PORT)}')

    # Kill the TX queue read
    self.commands_tx.put(THREAD_KILL)
    self.sock.close()
