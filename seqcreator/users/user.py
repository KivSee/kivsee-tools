from abc import abstractmethod
from seqcreator.network import manager


class User:

  @abstractmethod
  def __init__(self, name, thing_names):
      print(f"This is user: {name}")
      self.name = name
      self.thing_names = thing_names
      # TODO sapir add song mapping
      # self.songs_mapping = songs

  def get_elements(self):
      return self.thing_names

  def get_segments(self, thing_name):
      return manager.get_segments(thing_name)

  def play(self, trigger_name):
      raise Exception(f"{trigger_name} - not supported by parent class")
