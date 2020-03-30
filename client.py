from threading import Thread
import time
from service import TemperatureService, HumidityService

class Client(Thread):

  def __init__ (self, connection, client):
    Thread.__init__(self)
    print('Conectado por', client)
    self.connection = connection
    self.client = client
    self.status = None

    msg = connection.recv(1024)

    if(len(msg.split()) != 3):
      print('Comando invalido', msg)
      connection.close()
      return

    [conName, cmd, serviceName] = msg.split()

    if(cmd != b'CONECTAR'):
      print('Comando invalido', msg)
      connection.close()
      return

    if(serviceName == b'Temperatura_1' or serviceName == b'Temperatura_2'):
      self.service = TemperatureService()
    elif (serviceName == b'Umidade'):
      self.service = HumidityService()
    else:
      self.connection.send('Serviço não encontrado'.encode())

    if(self.service):
      name, status, temp = self.service.getStatus()
      self.status = status
      self.temp = temp

      self.connection.send(f'{name} {status} {temp}'.encode())

  def run(self):
    while self.status == 'ATIVADO':
      time.sleep(self.temp)

      self.connection.send(str(self.service.getValue()).encode())

    print('Finalizando conexao', self.client)
    self.connection.close()
