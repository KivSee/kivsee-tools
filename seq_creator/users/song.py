from network import manager

class Song(object):
    def __init__(self, user, trigger, duration):
      self.user = user
      self.trigger_name = trigger
      self.duration = duration
      self.effects_list = []

    def render_effects(self):
        # stub, overing in child impl
        pass

    def render(self):
        self.render_effects()
        return {
          "effects": self.effects_list,
          "duration_ms": self.duration,
          "num_repeats": 0
}

    def load(self):
      manager.store_sequence_all(self.trigger_name, self.render(), self.user.get_elements())


    def play(self):
        self.load()
        manager.play_song(self.trigger_name)
