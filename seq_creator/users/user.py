from network import manager

class User:
  def __init__(self, name, thing_names):
      print(f"User: {name}")
      self.name = name
      self.thing_names = thing_names

  def get_elements(self):
      return self.thing_names

  def get_segments(self, thing_name):
      return manager.get_segments(thing_name)