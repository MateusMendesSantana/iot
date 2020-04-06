import sys
import socket
import threading
from truck import Truck
from utils import openConfig
from env import CENTRAL_ID, ID, HOST, PORT


centrals = openConfig('centrals.txt')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

central = centrals[CENTRAL_ID]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con = s.connect((central['host'], central['port']))
s.send((f'LIVRE {ID}\n\n').encode())
s.close()

truck = Truck(tcp, ID)
truck.start()

input('Pressione qualquer tecla para encerrar a aplicação')

truck.running = False

tcp.close()