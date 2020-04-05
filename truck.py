from threading import Thread
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

  def __init__ (self, tcp):
    Thread.__init__(self)
    self.tcp = tcp

    print(img)
    
  def run(self):
    while True:
      connection, client = self.tcp.accept()
      Client(connection, client).start()

  def alertContainer(self, id):
    config = openConfig('containers.txt')
    container = config[id]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect((container['host'], container['port']))
    s.send((f'CHEGUEI_CONTAINER {id}\n\n').encode())
    s.close()
