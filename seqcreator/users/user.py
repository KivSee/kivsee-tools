from abc import abstractmethod
from seqcreator.elements.element_provider import ElementProvider
from seqcreator.logging.logger import kivsee_logger as logger

class User:

    @abstractmethod
    def __init__(self, name, all_things, all_segments):
        self.name = name
        # TODO this is temporary, until we retreive the segments from the led-objects-service
        self.element_provider = ElementProvider(name, all_things, all_segments)

    def play(self, trigger_name):
        raise Exception(f"{trigger_name} - not supported by parent class")
