from abc import ABC, abstractmethod
from seqcreator.infra.logger import kivsee_logger as logger


class ElementProvider(ABC):

    def __init__(self, user_name):
        self._user_name = user_name
    
    @abstractmethod
    def current_segments(self):
        """Provides the current semgments to be rendered.

        Returns:
            list: [('thing_name', 'segment_name'), ('thing_name', 'segment_name')]
        """

_ELEMENTS = None

def set_element_provider(elements_provider: ElementProvider):
    global _ELEMENTS
    _ELEMENTS = elements_provider

def get_element_provider() -> ElementProvider:
    return _ELEMENTS
