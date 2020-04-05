from threading import Thread
from random import choice, randrange
import time

class Client(Thread):

  def __init__ (self, connection, client):
    Thread.__init__(self)
    print('Conectado por', client)
    self.connection = connection
    self.client = client


  def run(self):
    msg = self.connection.recv(1024)

    [cmd, content] = msg.split()

    if(cmd == b'COLETAR'):
      temp = randrange(5, 20, 1)
      self.connection.send(f'{temp}\n\n'.encode())
      self.connection.close()
      time.sleep(temp)

    self.connection.close()
