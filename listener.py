from threading import Thread
from client import Client

class Listener(Thread):

  def __init__ (self, tcp):
    Thread.__init__(self)
    self.tcp = tcp

    print('Ouvindo conexões ;D')
    
  def run(self):
    while True:
      connection, client = self.tcp.accept()
      Client(connection, client).start()


