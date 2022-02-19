from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self, trigger_name):
        """Invoke the requested trigger

        Args:
            trigger_name (string): the trigger to invoke, either a song or soundless 
            animation that is implemented by this secuence creator.
        """
 