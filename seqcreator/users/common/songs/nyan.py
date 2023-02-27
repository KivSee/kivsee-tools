import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.rendering.functions.functions_store import const_function

import random

wingl = ("peacock1", "wing_l")
wingl_r = ("peacock1", "wing_l_r")
wingl_a1 = ("peacock1", "wing_l_a1")
wingl_a2 = ("peacock1", "wing_l_a2")
wingl_d = ("peacock1", "wing_l_d")
wingl_s = ("peacock1", "wing_l_s")
body = ("peacock1", "body")
head = ("peacock1", "head")
tail = ("peacock1", "tail")
all = [wingl, body, head, tail]

class Nyan(Song):
    def __init__(self):
        super().__init__("nyan", 2.45*60*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=8, start_offset=0)

        for ep in range(1, 17*3):
            timing.episode(ep)
            self.elements.set([wingl])
            self.rainbow_color()

            self.elements.set([wingl_a1])
            timing.cycle(1)
            masking.brightness_saw(0.3)
            self.elements.set([wingl_a2])
            timing.cycle(4)
            masking.brightness_saw(0)

        # for ep in range(1, 17*3):
        #     timing.episode(ep)

        #     self.elements.set([wingl_a1])
        #     self.rainbow_color()
        #     self.elements.set([wingl_a2])
        #     self.white()

        # all first section
        # timing.episodes(1, 17*3)

        # timing.cycle(4)
        # self.elements.set([wingl_s])
        # masking.snake()
        # masking.brightness_saw(0)

        # timing.cycle(1)
        # self.elements.set([wingl_a1])
        # masking.brightness_saw(0.5)


        return

        beats = 8
        hue = 0.05

        for x in range(2, 50, beats):
            timing.beats(x, x+beats)    
            masking.brightness_saw(0.0, 1.0, 10)
            hue += 0.25
            coloring.uniform(color.Color(hue))
        
        beats = 1
        for x in range(52, 80, beats):
            timing.beats(x, x+beats)    
            hue += 0.3
            coloring.uniform(color.Color(hue))

        beats = 8
        for x in range(80, 112, beats):
            timing.beats(x, x+beats)    
            hue += 0.2
            coloring.uniform(color.Color(hue))
        
        timing.beats(80, 112) 
        timing.cycle(4)
        # masking.hue_shift(0.4)
        masking.brightness_saw(0.0, 1.0, 10)
        # masking.saturation_shift(0.6)

        beats = 25
        for x in range(11200, 11600, beats):
            timing.beats(x/100, (x+beats)/100)    
            hue += 0.25
            coloring.uniform(color.Color(hue))

        # beats = 4
        # for x in range(116, 180, beats):
        #     timing.beats(x, x+beats)    
        #     hue += 0.1
        #     coloring.rainbow(hue, hue + 0.4)

        timing.beats(116, 180) 
        coloring.rainbow(0.0, 1.0, 1, 30)
        # timing.cycle(1)
        # masking.brightness_saw(0.8)
        
        # timing.beats(0, 130)    
        # masking.brightness(0.8)

    def white(self):
        coloring.uniform(color.Color(random.uniform(0.0, 1.0), 0.0, 0.7))

    def uniform_color(self):
        coloring.uniform(color.Color(random.uniform(0.0, 1.0), random.uniform(0.8, 1.0), 1.0))

    def rainbow_color(self):
        start = random.uniform(0.0, 1.0)
        coloring.rainbow_static(start, start + 1.0)

    def grad(self):
        start = random.uniform(0.0, 1.0)
        coloring.rainbow_static(start, start + 0.5)

    def segments_color(self):
        # self.elements.set([("peacock1", "head")])
        coloring.uniform(color.Color(random.uniform(0.0, 1.0), random.uniform(0.8, 1.0), 1.0))

    # same color different sat for each segment
    # 2 colors on segments from list of good looking options
    # full rainbow
    # small range rainbow
    # 

    def set_random_coloring(self):
        coloring_func = random.choice([self.grad])
        # coloring_func = random.choice([self.uniform_color, self.rainbow_color, self.segments_color, self.grad])
        coloring_func()
