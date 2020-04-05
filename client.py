from threading import Thread
from random import choice, randrange
from env import CENTRAL_ID
import time


class Client(Thread):

  def __init__(self, connection, client, truck):
    Thread.__init__(self)
    print('Conectado por', client)
    self.connection = connection
    self.client = client
    self.truck = truck

  def run(self):
    msg = self.connection.recv(1024).decode("utf-8")

    [cmd, conteinerId] = msg.split()

    if(cmd == 'COLETAR'):
      temp = randrange(5, 20, 1)
      self.connection.send(f'{temp}\n\n'.encode())
      self.connection.close()
      print(f'Dirigindo-se ao conteiner {conteinerId}, chega em {temp}')
      time.sleep(temp)
      print(f'Chegada ao conteiner {conteinerId}')
      self.truck.alertContainer(conteinerId)
      print(f'Retornando a central {CENTRAL_ID}, chegada em {temp}')
      time.sleep(temp)
      print(f'Coleta finalizada {CENTRAL_ID}')
      self.truck.finalizeDelivery()
