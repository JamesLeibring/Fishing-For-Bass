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

    print(f'Server started on {self.HOST}:{self.PORT}')

    # Queue of commands to broadcast
    self.commands:list[queue.Queue[str]] = []

    # Listen for X clients
    self.sock.listen(num_connections)

    for _ in range(num_connections):
      # Accept a new client connection
      client_socket, client_address = self.sock.accept()

      # Create a queue for commands sent to this socket
      client_queue:queue.Queue[str] = queue.Queue()
      self.commands += [client_queue]

      print(f'Connection made at {client_address}')

      # Create a new thread to handle the client connection
      threading.Thread(target=self.rx, args=(client_socket, client_address)).start()
      threading.Thread(target=self.tx, args=(client_socket, client_address, client_queue)).start()

  def rx(self:Server, sock:socket.socket, address:socket._RetAddress) -> None:
    # Listen to a client
    try:
      while True:
        # Receive message from the client
        message = sock.recv(1024).decode('utf-8')

        # Queue the command to be broadcast
        self.queue_cmd(message)
    except ConnectionResetError:
      print(f'Connection closed at {address}')
      sock.shutdown(socket.SHUT_RD)
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
      print(f'Connection closed at {address}')
      sock.shutdown(socket.SHUT_WR)

  def queue_cmd(self:Server, cmd:str) -> None:
    for q in self.commands:
      q.put(cmd)

  def close(self:Server) -> None:
    # Kill all TX queue reads
    self.queue_cmd(THREAD_KILL)

class Client:

  HOST = Server.HOST
  PORT = Server.PORT

  def __init__(self:Client) -> None:
    # Create the client socket and connect to host
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((Client.HOST, Client.PORT))

    print(f'Connection made at {(Client.HOST, Client.PORT)}')

    self.commands_tx:queue.Queue[str] = queue.Queue()
    self.commands_rx:queue.Queue[str] = queue.Queue()

    # Start TX/RX communications
    threading.Thread(target=self.tx).start()
    threading.Thread(target=self.rx).start()

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
      print(f'Connection closed at {(Client.HOST, Client.PORT)}')
      self.sock.shutdown(socket.SHUT_WR)

  def rx(self:Client) -> None:
    try:
      while True:
        # Receive command from server
        cmd = self.sock.recv(1024).decode('utf-8')

        # Queue the command recieved
        self.commands_rx.put(cmd)
    except ConnectionResetError:
      print(f'Connection closed at {(Client.HOST, Client.PORT)}')
      self.sock.shutdown(socket.SHUT_RD)
    except ConnectionAbortedError:
      pass

  def close(self:Client) -> None:
    # Kill the TX queue read
    self.commands_tx.put(THREAD_KILL)

    # Close the socket
    self.sock.close()
