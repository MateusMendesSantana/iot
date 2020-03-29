import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

while(True):
  msg = input('Digite uma mensagem:')

  if(msg == 'exit'):
    break

  tcp.send(msg.encode())

tcp.close()
