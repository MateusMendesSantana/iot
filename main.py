import sys
import socket
import threading
from truck import Truck
from utils import openConfig

HOST = ''
PORT = 5000
ID = '3'

centrals = openConfig('centrals.txt')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

central = centrals['0']

con = tcp.connect((central['host'], central['port']))
tcp.send((f'LIVRE {ID}\n\n').encode())

truck = Truck(tcp, ID)
truck.start()

input('Pressione qualquer tecla para encerrar a aplicação')

truck.running = False

tcp.close()