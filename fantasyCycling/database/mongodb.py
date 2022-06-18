from mongodb import MongoClient

class MongoDB:
  client = MongoClient()
  db = client.get_datbase('test')

def test():
  pass