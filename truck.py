from threading import Thread
from random import randrange
from client import Client
from utils import openConfig
import socket

img = """
   ___________________________  .
  |---------------------------|_:::..
  |>   ______  [IOT]  ______ <|||¨|¨\\___
  |•__/______\______ /______\_|)       \•]
  '¨¨*!(@)#(@)*¨¨¨¨¨*=!(@)#(@)=======!(@)''
"""


class Truck(Thread):

  def __init__(self, tcp, id):
    Thread.__init__(self)
    self.tcp = tcp
    self.id = id
    self.running = True

    print(img)

  def run(self):
    while self.running:
      connection, client = self.tcp.accept()
      Client(connection, client, self).start()

  def alertContainer(self, conteinerId):
    print(f'Esvaziando conteiner {conteinerId}')
    containers = openConfig('containers.txt')
    container = containers[conteinerId]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect((container['host'], container['port']))
    s.send((f'CHEGUEI_CONTAINER {conteinerId}\n\n').encode())
    s.close()

  def finalizeDelivery(self):
    centrals = openConfig('centrals.txt')
    centralId = randrange(0, len(centrals) - 1, 1)
    print(f'Coleta finalizada {centralId}')
    container = centrals[id]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect((container['host'], container['port']))
    s.send((f'COLETA_FINALIZADA {self.id}\n\n').encode())
    s.close()
