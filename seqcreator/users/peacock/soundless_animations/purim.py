
import random
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing
from seqcreator.api import coloring, masking
from seqcreator.api import element_provider
from seqcreator.api.color import Color
from seqcreator.rendering.functions.functions_store import const_function

wings = [("peacock1", "wing_l"), ("peacock1", "wing_r")]
torso = [("peacock1", "body"), ("peacock1", "head"), ("peacock1", "tail"),]
each = [("peacock1", "wing_l"), ("peacock1", "wing_r"), ("peacock1", "body"), ("peacock1", "head"), ("peacock1", "tail"), ]
all = [("peacock1", "all")]
# wings = [("peacock1", "wing_l"), ("peacock1", "wing_r")]
# wings = [("peacock1", "wing_l"), ("peacock1", "wing_r")]

def as_alternate_1(elements):
    return [("peacock1", f"{e[1]}_a1") for e in elements]

def as_alternate_2(elements):
    return [("peacock1", f"{e[1]}_a2") for e in elements]

def as_symmetric(elements):
    return [("peacock1", f"{e[1]}_s") for e in elements]

def as_random(elements):
    return [("peacock1", f"{e[1]}_r") for e in elements]

class Purim(SoundlessAnimation):
    def __init__(self):
        super().__init__("purim", 1000 * 60 * 20, 0)
        self.elements = element_provider.get_element_provider()

    def alternate_coloring(self):
        [hue, sat] = [random.random(), random.uniform(0.7, 1.0)]
        self.elements.set([("peacock1", "all_a1")])
        coloring.uniform(Color(hue + 0.15, 0.7, 0.5))
        self.elements.set([("peacock1", "all_a2")])
        coloring.uniform(Color(hue, 1.0, 0.5))

    def coloring_uniform(self):
        [hue] = [random.random()]
        self.elements.set(wings)
        coloring.uniform(Color(hue + 0.07, 0.75, 0.5))
        self.elements.set(torso)
        coloring.uniform(Color(hue, 1.0, 0.5))

    def party(self):
        self.elements.set(each)
        coloring.rainbow_static(0, 3)

    def party_alternate(self):
        [hue] = [random.random()]
        self.elements.set(as_alternate_1(all))
        coloring.rainbow_static(hue + 0, hue + 1.0)
        self.elements.set(as_alternate_2(all))
        coloring.rainbow_static(hue + 0.08, hue + 1.08)

    def apply_random_coloring(self):
        random_coloring = random.choice([
            self.alternate_coloring,
            self.coloring_uniform,
            self.party,
            self.party_alternate,
        ])

        random_coloring()

    def snake(self):
        self.elements.set(as_symmetric(each))
        masking.snake()

    def twinkle(self):
        self.elements.set(as_random(all))
        masking.snake()

    def snake_alternate(self):
        self.elements.set(as_alternate_1(each))
        masking.snake()

    def alternate(self):
        self.elements.set(as_alternate_1(all))
        masking.brightness_sin(0.1, 1)
        self.elements.set(as_alternate_2(all))
        masking.brightness_sin(1, 0.1)

    def pulse(self):
        self.elements.set(all)
        masking.brightness_sin(0.2, 1)

    def apply_random_effect(self, cycle):
        random_effect = random.choice([
            self.snake,
            self.snake_alternate,
            self.alternate,
            self.pulse,
            self.twinkle,
        ])

        # self.elem(cycle)
        random_effect()

    def set_4episodes_coloring(self, e: int):
        timing.episodes(e, e + 4)
        self.apply_random_coloring()

    def set_effect(self, e: int):
        timing.episode(e)
        cycle = random.choice([1,2,4,8])
        timing.cycle(cycle)
        self.apply_random_effect(cycle)


    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        for e in range(0, 80, 4):
            self.set_4episodes_coloring(e)
        for e in range(0, 80, 1):
            self.set_effect(e)
