from abc import ABC

class User(ABC):

    def __init__(self, name):
        self.name = name

    def play(self, trigger_name):
        raise Exception(f"{trigger_name} - not supported by parent class")
