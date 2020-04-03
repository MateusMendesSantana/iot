import sys
import socket
import threading
from listener import Listener

HOST = ''
PORT = int(input('Informe sua porta:'))

def openConfig():
  f = open("lista_dispositivos.txt", "r")

  data = f.read().splitlines()
  data = list(map(lambda str: str.split(), data))

  devices = {}

  for item in data:
    devices[item[0]] = {
      'host': item[1],
      'port': int(item[2])
    }

  return devices

""" def cleanMsg(msg):
  return msg.re """

devices = openConfig()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

listener = Listener(tcp)
listener.start()   

while True:
  msg = input('Digite uma nova conexão {NOME} CONECTAR {SERVICO}:')

  if(msg == 'exit'):
    break
    
  das = msg.split()

  if(len(das) == 3 and das[1] == 'CONECTAR'):
    config = devices[das[2]]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect((config['host'], config['port']))
    s.sendall((msg+'\n\n').encode())
    msg = s.recv(1024)
    das = msg.split()
    print(msg)

    if(das[1] == b'ATIVADO'):
      while True:
        msg = str(s.recv(1024), 'utf-8', 'ignore')

        if(msg != ''):
          print(msg)
    else:
      print('Conexão encerrada pois o serviço esta DESATIVADO')
      s.close()
  else:
    print('Comando desconhecido')

tcp.close()