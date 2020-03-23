import socket
import threading

HOST = ''
PORT = 5000

def conectado(con, cliente):
  print('Conectado por', cliente)

  while True:
    msg = con.recv(1024)

    if not msg:
      break

    print(cliente, msg)

  print('Finalizando conexao do cliente', cliente)
  con.close()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

print('Ouvindo conexões ;D')

while True:
  con, cliente = tcp.accept()
  con.sendall('Mateus - All clear \n\n'.encode())
  threading._start_new_thread(conectado, tuple([con, cliente]))

tcp.close()
