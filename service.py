from random import choice, randrange

class TemperatureService(): 

  def getStatus(self):
    name = choice(['Temperatura_1', 'Temperatura_2'])
    status = choice(['ATIVADO ', 'DESATIVADO'])
    temp = randrange(10, 45, 1)

    return name, status, temp

  def getValue(self):
    return randrange(20, 45, 1)

class HumidityService(): 

  def getStatus(self):
    status = choice(['ATIVADO ', 'DESATIVADO'])
    temp = randrange(10, 45, 1)

    return 'Umidade', status, temp

  def getValue(self):
    return randrange(0, 100, 5)