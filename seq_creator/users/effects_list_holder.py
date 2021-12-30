class EffectsListHolder:
    def __init__(self):
        self._effects_list = []

    @property
    def effects_list(self):
        return self._effects_list

    def extend(self, arr):
        self._effects_list.extend(arr)

    def __getitem__(self, idx):
        print("getitem")
        return self._effects_list[idx]

    def __setitem__(self, idx, value):
        print("setitem")
        self._effects_list[idx] = value