from abc import abstractmethod
from infra.animations_factory import ColoringEffectFactory
from network import manager

from users.effects_list_holder import EffectsListHolder


class Song(object):

    # @abstractmethod
    def __init__(self, trigger, duration, repeats, thing_names):
        self.trigger_name = trigger
        self.duration = duration
        self.holder = EffectsListHolder()
        self.repeats = repeats
        self.thing_names = thing_names
        self.segments = ["spiral1"]  # manager.get_segements(thing_name) fo thing_name in thing_names
        self.coloring_effect = ColoringEffectFactory(self.segments, self.holder)



    def render_effects(self):
        # stub, overing in child impl
        print("song::render_effects")
        pass


    def render(self):
        self.render_effects()
        return {
            "effects": self.holder.effects_list,
            "duration_ms": self.duration,
            "num_repeats": self.repeats
        }


    def store_sequence(self):
        # print(f"storing for each element in {self.user.get_elements()}")
        seq = self.render()
        manager.store_sequence_all(self.trigger_name, seq, self.thing_names)


    def play(self):
        print(f"Song: load {self.trigger_name}")
        self.store_sequence()
        print(f"Song: playing {self.trigger_name}")
        manager.play_song(self.trigger_name)
