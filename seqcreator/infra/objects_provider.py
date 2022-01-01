class ObjectsProvider:
        def __init__(self):
            self._elements = ["all"]

        @property
        def elements(self):
            return self._elements

        @elements.setter
        def elements(self, value):
            self._elements = value

        def __getitem__(self, idx):
            return self._elements[idx]

        def __setitem__(self, idx, value):
            self._elements[idx] = value