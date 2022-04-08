from abc import ABC, abstractmethod
import json
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger


class ElementProvider(ABC):

    def __init__(self, user_name):
        self.current = []
        self._user_name = user_name
        self.all_segments = []
    
    
    def fetch_all_tuples(self) -> list:
        """Gets things info from the led object service, extracts the segment names
        and returns an list of tuples of thing name and segment name.

        Returns:
            list: returns a list of tuples [(thing_name, segment_name), (thing_name, segment_name), ...]
        """
        all_segments_json = network_manager.get_all_segments()
        result = []
        things = json.loads(all_segments_json)
        for (thing, body) in things.items():
            for (thing_info, val) in body.items():
                if (thing_info == "segments"):
                    for segments in val:
                        for segment_name in segments.values():
                            result.append((thing, segment_name))
        return result

    def fetch_all_things(self) -> list:
        all_segments_json = network_manager.get_all_segments()
        result = []
        things = json.loads(all_segments_json)
        for (thing, body) in things.items():
            result.append((thing, "all"))
        print(result)    
        return result

    
    def set(self, tuples):
        """Sets the current segments the animation is processed on.

        Args:
            tuples (list): list of tuples [(thing_name, segment_name), ...]
        """
        self.current = tuples
    
    def all(self):
        """ Returns tuples of things with a segment named "all"

        Returns:
            tuples (list): list of tuples [(thing_name, "all"), (thing_name, "all") ...]
        """
        self.all_things = self.fetch_all_things()
        return self.all_things
        
    def current_segments(self):
        """Returns the current segements that animation should be processed on.

        Returns:
            list: list of tuples [(thing_name, segment_name), ...]
        """
        return self.current
    
    def get_all_segments(self):
        if len(self.all_segments) == 0:
            self.all_segments = self.fetch_all_tuples()
        return self.all_segments

    def all_even(self):
        """Returns all even segments

        Returns:
            list: returns a list of tuples [(thing_name, segment_name), (thing_name, segment_name), ...]
        """
        return self.get_all_segments()[::2]

    def all_odd(self):
        """Returns all odd segments

        Returns:
            list: returns a list of tuples [(thing_name, segment_name), (thing_name, segment_name), ...]
        """
        return self.get_all_segments()[1::2]

_ELEMENTS = None

def set_element_provider(elements_provider: ElementProvider):
    global _ELEMENTS
    _ELEMENTS = elements_provider

def get_element_provider() -> ElementProvider:
    return _ELEMENTS
