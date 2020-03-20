from threading import Thread
import time
from service import TemperatureService, HumidityService

class Client(Thread):

  def __init__ (self, connection, client):
    Thread.__init__(self)
    print('Conectado por', client)
    self.connection = connection
    self.client = client

    msg = connection.recv(1024)

    [conName, cmd, serviceName] = msg.split()

    if(cmd != 'CONECTAR'):
      self.connection.send('Comando invalido')
      return

    if(serviceName == 'Temperatura_1' or serviceName == 'Temperatura_2'):
      self.service = TemperatureService()
    elif (serviceName == 'Umidade'):
      self.service = HumidityService()
    else:
      self.connection.send('Serviço não encontrado')

    if(self.service):
      name, status, temp = self.service.getStatus()
      self.status = status
      self.temp = temp

      if(status == 'ATIVADO'):
        self.connection.send(f'{name} {status} {temp}')
      else:
        self.connection.send('DESATIVADO')

  def run(self):
    while self.status == 'ATIVADO':
      time.sleep(self.temp)

      self.connection.send(self.service.getValue())

    print('Finalizando conexao', self.client)
    self.connection.close()
