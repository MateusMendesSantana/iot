import json

with open('config.json') as json_file:
  config = json.load(json_file)

CENTRAL_ID = config['CENTRAL_ID']
HOST = config['HOST']
PORT = config['PORT']
ID = config['ID']
