import sys
import socket
import threading
from listener import Listener

HOST = ''
PORT = 5000

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
    con = tcp.connect((config['host'], config['port']))
    con.send(msg)
  else:
    print('Comando desconhecido')

tcp.close()