def openConfig(file):
  f = open(file, "r")

  data = f.read().splitlines()
  data = list(map(lambda str: str.split(), data))

  devices = {}

  for item in data:
    devices[item[0]] = {
      'host': item[1],
      'port': int(item[2])
    }

  return devices