from seqcreator.network import manager
from seqcreator.logging.logger import kivsee_logger as logger


class ElementProvider:

    def __init__(self, user_name, all_things, all_segements):
        self._user_name = user_name
        self._all_things = all_things
        self._all_segments = all_segements

    def all_things(self):
        return self._all_things

    def get_segments(self, thing_name):
        return manager.get_segments(thing_name)

    def all_segments(self):
        return self._all_segments
