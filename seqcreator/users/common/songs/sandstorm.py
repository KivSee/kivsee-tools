import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.api.sandstorm_coloring import get_random_coloring, gradient, rainbow, uniform
from seqcreator.api.sandstorm_masking import alternate_blink, alternate_sin, blink_group, brightness_saw_rising, brightness_sin, get_random_masking, snake_grow_shrink, snake_step
from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.rendering.effects.snake import SnakeEffect
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, steps_function

import random

from seqcreator.segment_utils import as_symmetric

wingl = ("peacock1", "wing_l")
wingr = ("peacock1", "wing_r")
wingl_r = ("peacock1", "wing_l_r")
wingl_a1 = ("peacock1", "wing_l_a1")
wingl_a2 = ("peacock1", "wing_l_a2")
wingl_d = ("peacock1", "wing_l_d")
wingl_s = ("peacock1", "wing_l_s")
wing_r = ("peacock1", "wing_r")
wing_l = ("peacock1", "wing_l")

body = ("peacock1", "body")
body_r = ("peacock1", "body_r")
body_d = ("peacock1", "body_d")
body_a1 = ("peacock1", "body_a1")
body_a2 = ("peacock1", "body_a2")
body_s = ("peacock1", "body_s")
head = ("peacock1", "head")
tail = ("peacock1", "tail")
wing_l_s = ("peacock1", "wing_l_s")
wing_r_s = ("peacock1", "wing_r_s")
crown = ("peacock1", "crown")
neck = ("peacock1", "neck")
neck_a1 = ("peacock1", "neck_a1")
neck_a2 = ("peacock1", "neck_a2")
all = [wingl, wingr, body, head, tail]

class Sandstorm(Song):
    def __init__(self):
        super().__init__("sandstorm", (5 + 5/60)*60*1000, 0)
        self.elements = element_provider.get_element_provider()

    def get_hues(self):
        hue = random.random()
        return [hue, hue + 0.15] 

    def coloring_uniform(self, hue1):
        self.elements.set(all)
        coloring.uniform(color.Color(hue1, 1.0, 1.0))

    def grad(self, hue1):
        self.elements.set(as_symmetric(all))
        coloring.rainbow_static(hue1, hue1 + 0.2)

    def hue_shift(self):
        self.elements.set([wingl, wingr])
        masking.hue_shift_const(0.15)

    def sat_shift(self):
        self.elements.set([wingl, wingr])
        masking.saturation(0.75)

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=16, start_offset=0)

        self.color_section(0, 4) #peak 4-5
        self.color_section2(4, 6)
        self.color_section(6, 8) #peak 9
        self.color_section_beat(8, 10) 
        #self.color_section2(7, 10)
        self.color_section3(10, 14) #peak 13
        self.sandstorm_peak(14)
        #self.color_section(13, 17) #peak 17 highlight of song
        self.color_section(17, 21) #peak 19
        self.color_section(21, 23) # similar to 0-5
        self.color_section(23, 25) #calm
        self.color_section(25, 29) #highlight of song
        #self.color_section(29, 33.5) #similar to 17-21
        #self.color_section(33.5, 40) #similar to 0-5

    def basic_effect(self):
        timing.cycle(16)
        #get_effects().add_effect(SnakeEffect(steps_function(8, 0.125, 0.125), const_function(8.0)))
        get_effects().add_effect(SnakeEffect(steps_function(8, 0.125, 0.125), const_function(0.125)))

    def sandstorm_peak(self, ep):
        [hue1, hue2] = self.get_hues()
        self.elements.set([("peacock1","all")])
        timing.episodes(14, 15)
        get_effects().add_effect(ConstColor(color.Color(0.333)))
        timing.cycle(2)
        blink_group(self.elements, {})
        get_random_coloring(self.elements, {'hue': hue1, 'hue2': hue2, 'intensity': 0.25})
        timing.cycle(6)
        snake_grow_shrink(self.elements, {}) 
        get_effects().add_effect(ConstColor(color.Color(0.333)))
        timing.cycle(2)
        blink_group(self.elements, {})    
        get_random_coloring(self.elements, {'hue': hue1, 'hue2': hue2, 'intensity': 0.25})
        timing.cycle(6)
        snake_grow_shrink(self.elements, {})    

    def color_section(self, start_ep, end_ep):
        [hue1, hue2] = self.get_hues()        
        # timing.episodes(start_ep, end_ep)
        for e in range (start_ep, end_ep, 1):        
            timing.episodes(e, e+1)
            self.elements.set([wing_l_s, wing_r_s])
            #self.basic_effect()
            uniform(self.elements, {})
            timing.cycle(2)
            snake_grow_shrink(self.elements, {})
            #get_effects().add_effect(ConstColor(color.LIGHT_TURQUOISE))
            #get_random_coloring(self.elements, {'hue': hue1, 'hue2': hue2, 'intensity': 0.25})
            #get_random_masking(self.elements, {})  

    def color_section2(self, start_ep, end_ep):    
        timing.episodes(start_ep, end_ep)
        self.elements.set([wingl, wingr])
        uniform(self.elements, {})
        alternate_blink(self.elements, {})
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        #timing.cycle(4)
        get_effects().add_effect(ConstColor(color.Color(0.8)))
        alternate_sin(self.elements, {})
        

    def color_section3(self, start_ep, end_ep):    
        timing.episodes(start_ep, end_ep)
        self.elements.set([wingl, wingr])
        rainbow(self.elements, {})
        alternate_blink(self.elements, {})
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        rainbow(self.elements, {})   
        alternate_sin(self.elements, {})

    def color_section_beat(self, start_ep, end_ep):    
        timing.episodes(start_ep, end_ep)
        self.elements.set([wingl, wingr])
        uniform(self.elements, {})
        alternate_blink(self.elements, {})
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        #timing.cycle(4)
        get_effects().add_effect(ConstColor(color.Color(0.8)))
        alternate_blink(self.elements, {})
