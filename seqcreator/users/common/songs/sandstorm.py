import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.api.sandstorm_coloring import get_random_coloring, gradient, rainbow, uniform
from seqcreator.api.sandstorm_masking import alternate_blink, alternate_sin, blink_group, brightness_saw_rising, brightness_sin, get_random_masking, half_alternate_blank, half_alternate_blink, half_alternate_sin, snake_grow_shrink, snake_step
from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.rainbow import Rainbow
from seqcreator.rendering.effects.saturation import Saturation
from seqcreator.rendering.effects.snake import SnakeEffect
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, half_function, linear_function, repeat_function, sin_function, sin_start_max, sin_start_min, steps_from_to, steps_function
from seqcreator.rendering.effects.brightness import Brightness as BrightnessEffect 

import random

from seqcreator.segment_utils import as_symmetric
from seqcreator.users.common.songs.req import color_red, color_white

wingl = ("peacock1", "wing_l")
wingr = ("peacock1", "wing_r")
wingl_r = ("peacock1", "wing_l_r")
wingl_a1 = ("peacock1", "wing_l_a1")
wingl_a2 = ("peacock1", "wing_l_a2")
wingl_d = ("peacock1", "wing_l_d")
wingl_s = ("peacock1", "wing_l_s")
wing_r = ("peacock1", "wing_r")
wingr_d = ("peacock1", "wing_r_d")
wing_l = ("peacock1", "wing_l")

body = ("peacock1", "body")
body_r = ("peacock1", "body_r")
body_d = ("peacock1", "body_d")
body_a1 = ("peacock1", "body_a1")
body_a2 = ("peacock1", "body_a2")
body_s = ("peacock1", "body_s")
head = ("peacock1", "head")
head_d = ("peacock1", "head_d")
tail = ("peacock1", "tail")
tail_d = ("peacock1", "tail_d")
wing_l_s = ("peacock1", "wing_l_s")
wing_r_s = ("peacock1", "wing_r_s")
crown = ("peacock1", "crown")
neck = ("peacock1", "neck")
neck_a1 = ("peacock1", "neck_a1")
neck_a2 = ("peacock1", "neck_a2")
all_elements_a1 = [("peacock1", "all_a1")]
all_elements_a2 = [("peacock1", "all_a2")]
all = [wingl, wingr, body, head, tail]
no_head = [wingl, wingr, body, tail]
no_crown = [wingl, wingr, body, tail, neck]
all_s = [wing_l_s, wing_r_s, body, head, tail]
all_elements_single_sym = [("peacock1", "wing_l_s"), ("peacock1", "wing_r_s"), ("peacock1", "body_s"), ("peacock1", "tail_s"), ("peacock1", "head_s")]
all_d = [wingl_d, wingr_d, body_d, head_d, tail_d]

blink_min_val = 0.6
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

        
        self.sandstorm_beginning(0)
        self.sandstorm_peak(14)
        self.sandstorm_calm(23)
        self.sandstorm_peak2(26)
        self.sandstorm_after_peak_party(30.5) # 30.5 - 34.5
        self.sandstorm_basic_beat3(34.5)
        self.sandstorm_minimalist(38.5)
        
        #self.color_section(29, 33.5) #similar to 17-21
        #self.color_section(33.5, 40) #similar to 0-5

    def sandstorm_beginning(self, ep):
          # basic beat
        self.in_episodes(0, 4)
        self.elements.set([wing_l_s, wing_r_s])
        hue = uniform(self.elements, {})
        get_effects().add_effect(HueShift(steps_from_to(num_steps=8, start=0, end=0.6)))
        self.with_cycle(8, 0, 4)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(0, 1)), const_function(0.25), True))
        self.with_cycle(16, 4, 8)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 12, 16)
        get_effects().add_effect(SnakeEffect(repeat_function(4, linear_function(1, 0)), const_function(0.25), True))
        self.in_episodes(1,4)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 0.8)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=8, start=0, end=0.6)))
        self.with_cycle(16, 0, 12)
        self.sandstorm_blink(1)
        #self.sandstorm_alternate_blink(1)
        self.with_cycle(16, 12, 16)
        self.elements.set([body, head, tail])
        #get_effects().add_effect(HueShift(steps_from_to(num_steps=16, start=0, end=0.35)))
        alternate_blink(self.elements, 8)
        self.crown_flickering2(0, 2, True)
           # adding high pitch note sparkles
        self.in_episodes(4, 6)
        self.elements.set([("peacock1", "all_r")])
        rainbow(self.elements, {})
        self.with_cycle(32, 0, 12)
        get_effects().add_effect(Saturation(linear_function(1.0, 0.7)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.6, 0.8)))
        self.with_cycle(1.0)
        get_effects().add_effect(SnakeEffect(repeat_function(1, linear_function(0.5, 0)), linear_function(0.4, 0.6), True))
        # head back to previous head effect
        self.with_cycle(32, 12, 32)
        self.elements.set([head])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 0.8)))
        self.sandstorm_alternate_blink2(1)
        self.with_cycle(32, 24, 32)
        self.elements.set([body, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        self.sandstorm_alternate_blink2(1)
            # back to basic beat TODO: improve effects
        self.sandstorm_basic_beat(6)
            # increasing volume high pitch sound leading to peak
        #sparkles
        self.in_episodes(10, 13)
        self.elements.set([("peacock1","all")])
        rainbow(self.elements, {})
        self.elements.set([("peacock1","all_r")])
        get_effects().add_effect(Saturation(linear_function(0.7, 1.0)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.4, 0.9)))
        get_effects().add_effect(SnakeEffect(repeat_function(1, steps_from_to(32, 0, 1)), linear_function(0.05, 1.0), True))
        self.in_episodes(12, 14)
        self.elements.set([("peacock1","head")])
        rainbow(self.elements, {})
        get_effects().add_effect(BrightnessEffect(const_function(0.8)))
        self.with_cycle(2, 0, 0.25)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 1)))
        self.with_cycle(2, 0.75, 1.0)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect((sin_function(0.0, 0.4, 0, 1))))
        self.with_cycle(2, 1.5, 1.75)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect((sin_function(0.0, 0.4, 0, 1))))
        # self.in_episodes(13, 14)
        # self.elements.set([("peacock1","all_r")])
        # rainbow(self.elements, {})
        # #self.elements.set([("peacock1","all_r")])
        # get_effects().add_effect(BrightnessEffect(const_function(0.8)))
        # self.with_cycle(2, 0, 0.25)
        # self.elements.set(all_elements_a1)
        # get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 1)))
        # self.with_cycle(2, 0.75, 1.0)
        # self.elements.set(all_elements_a2)
        # get_effects().add_effect(BrightnessEffect((sin_function(0.0, 0.4, 0, 1))))
        # self.with_cycle(2, 1.5, 1.75)
        # self.elements.set(all_elements_a1)
        # get_effects().add_effect(BrightnessEffect((sin_function(0.0, 0.4, 0, 1))))

    def sandstorm_alternate_blink2(self, repeat_times): #TODO
        self.with_cycle(1, 0.0, 0.325)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.with_cycle(2, 1.25, 1.5)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
    
    def sandstorm_alternate_blink(self, repeat_times):
        self.with_cycle(1, 0.0, 0.125)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.with_cycle(4, 3.5, 3.75)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
    
    def sandstorm_alternate_blink3(self, repeat_times):
        self.with_cycle(1, 0.0, 0.125)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.with_cycle(4, 1.5, 1.675)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
    
    def sandstorm_alternate_blink4(self, repeat_times):
        self.with_cycle(1, 0.0, 0.125)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.with_cycle(4, 3.5, 3.675)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))

    def sandstorm_blink(self, repeat_times):
        self.with_cycle(1, 0.0, 0.125)
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))
        self.with_cycle(4, 3.5, 3.75)
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))
        self.with_cycle(16, 12, 16) #TODO
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(0.9)))))


    def sandstorm_peak(self, ep):
        self.elements.set([("peacock1","all")])
        self.in_episodes(14, 18)
        rainbow(self.elements, {})   
        self.in_episodes(14, 16)
        self.with_cycle(8, 0, 1)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(8, 1, 1.5)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
        self.with_cycle(8, 1.5, 8)
        alternate_sin(self.elements, 1)

# first beat of special tutututu
        self.in_beats(231, 232)
        self.elements.set([("peacock1","all")])
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
# alternate red blue special tutututu
        self.in_beats(247, 247.5)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        self.in_beats(247.5, 249)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        self.elements.set(all_elements_a2)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(6, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.in_beats(249, 250)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        self.elements.set(all_elements_a2)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(0.5), const_function(0.8))))

        self.in_episodes(16, 17)
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(4, 1, 1.5)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
        self.with_cycle(4, 1.5, 4)
        alternate_sin(self.elements, 1)
        self.in_episodes(17, 18)
        self.with_cycle(2, 0, 1)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(2, 1, 2)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
        self.with_cycle(16, 8, 12)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(32, half_function(const_function(blink_min_val), const_function(1.0)))))

        self.in_beats(284, 288)
        self.elements.set([("peacock1","all")])
        get_effects().add_effect(ConstColor(color.Color(0.66, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(16, 0, 0.65)))
        snake_step(self.elements, {})
          
        self.in_episodes(18, 21.5)
        rainbow(self.elements, {})
        self.with_cycle(2)
        self.elements.set([("peacock1", "wing_l"), ("peacock1", "wing_r")])
        get_effects().add_effect(SnakeEffect(linear_function(0.0, 1.0), const_function(0.75), True))
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(blink_min_val), const_function(0.5)))))

        self.in_episodes(18, 21.5)
        self.with_cycle(8, 7, 8)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))   

        #special tutu tu tutu
        self.in_beats(316, 320)
        self.with_cycle(2, 0, 0.25)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 1)))
        self.with_cycle(2, 0.75, 1.0)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect((sin_function(0.0, 0.4, 0, 1))))
        self.with_cycle(2, 1.5, 1.75)
        self.elements.set(all_elements_a1)
        rainbow(self.elements, {})
        get_effects().add_effect(BrightnessEffect((sin_function(0.0, 0.4, 0, 1))))

        # PEAK
        self.in_episodes(21.5, 22.5)
        self.elements.set([("peacock1", "all")])
        rainbow(self.elements, {})
        self.in_beats(344, 345)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 4)))
        self.in_beats(345, 352)
        self.with_cycle(2, 0.0, 0.125)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 1)))
        self.with_cycle(2, 0.5, 2.0)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 6)))
        
        self.in_beats(352, 354)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        #end of peak
        self.in_beats(352, 353)
        self.with_cycle(0.25, 0.125, 0.25)
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))
        self.in_beats(353, 354)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.0)))
        # back to basic beat
        self.sandstorm_basic_beat2(0)
        
    def sandstorm_calm(self, ep):
        self.in_episodes(24, 26)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        #get_effects().add_effect(BrightnessEffect(repeat_function(16, half_function(const_function(blink_min_val), const_function(1.0)))))
        get_effects().add_effect(HueShift(linear_function(0,-0.3)))
        get_effects().add_effect(SnakeEffect(steps_from_to(32, 0, 4), const_function(0.75), True))
        self.elements.set([("peacock1", "crown")])
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(const_function(0.0)))
        
        #crown flickering
        self.crown_flickering(24.5, 26, True)

    def sandstorm_after_peak_party(self, ep):
        self.in_episodes(ep, ep+4)
        self.elements.set([("peacock1", "all")])
        rainbow(self.elements, {})
        self.with_cycle(2)
        self.elements.set([("peacock1", "wing_l"), ("peacock1", "wing_r")])
        get_effects().add_effect(SnakeEffect(linear_function(0.0, 1.0), const_function(0.75), True))
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(blink_min_val), const_function(0.5)))))

        #red tudu beginning
        self.in_episodes(ep, ep+2)
        self.with_cycle(8, 7, 8)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.85, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))   

        #red tudu end  TODO
        self.in_episodes(ep+2, ep+3.5)
        self.with_cycle(8, 7, 8)
        self.elements.set([tail, body])
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.0, 0.0)))
        self.elements.set([("peacock1", "head_r")])#, ("peacock1", "body_r"), ("peacock1", "tail_r")])
        rainbow(self.elements, {})
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))   

        #special tutu tu tutu tu
        self.in_beats(516, 520)
        self.elements.set([("peacock1", "all_r")])
        # get_effects().add_effect(ConstColor(color.Color(0.0, 0.95, 1.0)))
        rainbow(self.elements, {})
        #self.with_cycle(1)
        #get_effects().add_effect(BrightnessEffect(sin_start_min(0.2, 0.9, 1)))
        self.sandstorm_alternate_blink(1)

        # basic PEAK sound
        self.elements.set([("peacock1", "all")])
        rainbow(self.elements, {})
        self.in_beats(548, 549)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 4)))
        self.in_beats(549, 552)
        self.with_cycle(2, 0.0, 0.5)
        self.elements.set(all_elements_a1)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 1)))
        self.with_cycle(2, 0.5, 2.0)
        self.elements.set(all_elements_a2)
        get_effects().add_effect(BrightnessEffect(sin_function(0.0, 0.4, 0, 6)))
        
    def crown_flickering(self, start_ep, end_ep, intensify=False):
        self.in_episodes(start_ep, end_ep)
        self.elements.set([("peacock1", "crown")])
        get_effects().add_effect(ConstColor(color.Color(0.0, 0.95, 1.0)))
        if intensify:
            get_effects().add_effect(BrightnessEffect(steps_from_to(32, 0.1, 0.9)))
        else:
            get_effects().add_effect(BrightnessEffect(const_function(0.9)))
        self.with_cycle(2, 0.0, 0.125)
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))
        self.with_cycle(2, 0.75, 0.875)
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))
        self.with_cycle(2, 1.5, 1.625)
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))

    def crown_flickering2(self, start_ep, end_ep, intensify=False):
        self.in_episodes(start_ep, end_ep)
        self.elements.set([("peacock1", "crown")])
        get_effects().add_effect(ConstColor(color.Color(0.0, 0.95, 1.0)))
        if intensify:
            get_effects().add_effect(BrightnessEffect(steps_from_to(32, 0.1, 0.9)))
        else:
            get_effects().add_effect(BrightnessEffect(const_function(0.9)))
        self.with_cycle(1, 0.0, 0.125)
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))
        self.with_cycle(4, 3.5, 3.75)
        get_effects().add_effect(BrightnessEffect(const_function(0.2)))
        self.with_cycle(16, 12, 16) #TODO
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(0.9)))))

#episdode 26 - 30.5
    def sandstorm_peak2(self, ep):
        #self.crown_flickering(26, 28, False)
        self.elements.set([("peacock1","all")])
        self.in_episodes(26, 28)
        rainbow(self.elements, {})   
        self.with_cycle(16, 0, 1)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(16, 1, 1.5)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
        self.with_cycle(16, 1.5, 16)
        get_effects().add_effect(HueShift(linear_function(0,-0.3)))
        get_effects().add_effect(SnakeEffect(steps_from_to(7, 0, 4), const_function(0.75), True))

        self.crown_flickering(26, 28, False)

        #faster tututu
        self.in_episodes(28, 30)
        self.elements.set([("peacock1","all")])
        rainbow(self.elements, {})
        get_effects().add_effect(HueShift(linear_function(0,-0.3)))
        get_effects().add_effect(SnakeEffect(steps_from_to(7, 0, 4), const_function(0.75), True))
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(4, 1, 1.5)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
        
        self.crown_flickering(28, 30, False)

        #faster tututu
        self.in_episodes(29, 29.5)
        self.elements.set([("peacock1","all")])
        rainbow(self.elements, {})
        get_effects().add_effect(HueShift(linear_function(0,-0.3)))
        #get_effects().add_effect(SnakeEffect(steps_from_to(7, 0, 4), const_function(0.75), True))
        self.with_cycle(2, 0, 1)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(2, 1, 1.5)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(half_function(const_function(blink_min_val), const_function(1.0))))
        
        #fastest tututu
        self.in_episodes(29.5, 30)
        self.elements.set([("peacock1","all")])
        rainbow(self.elements, {})
        get_effects().add_effect(HueShift(linear_function(0,-0.3)))
        #get_effects().add_effect(SnakeEffect(steps_from_to(7, 0, 4), const_function(0.75), True))
        self.with_cycle(1, 0, 0.5)
        get_effects().add_effect(ConstColor(color.Color(0.66, 0.8, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(1, 0.5, 1)
        rainbow(self.elements, {})
        get_effects().add_effect(BrightnessEffect(repeat_function(2, half_function(const_function(blink_min_val), const_function(1.0)))))

        #build up ep 30-30.5
        self.in_beats(480, 488)
        self.elements.set([("peacock1","head")])
        get_effects().add_effect(ConstColor(color.Color(0.0, 0.95, 1.0)))
        get_effects().add_effect(BrightnessEffect(const_function(0.9)))
        self.with_cycle(1)
        get_effects().add_effect(BrightnessEffect(repeat_function(4, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.with_cycle(2, 1, 1.5)
        get_effects().add_effect(ConstColor(color.Color(0.333, 0.95, 1.0)))

    def sandstorm_basic_beat(self, start_ep):
        self.in_episodes(start_ep, start_ep+2)
        self.elements.set([wing_l_s, wing_r_s])
        hue = uniform(self.elements, {})
        self.with_cycle(8, 0, 4)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(0, 1)), const_function(0.25), True))
        self.with_cycle(16, 4, 8)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 12, 16)
        get_effects().add_effect(SnakeEffect(repeat_function(4, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 0, 12)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        self.sandstorm_alternate_blink(1)
        self.with_cycle(16, 12, 16)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=16, start=0, end=0.35)))
        alternate_blink(self.elements, 8)
#TODO        
        self.in_episodes(start_ep+1, start_ep+2)
        self.elements.set([("peacock1","all")])
        hue = uniform(self.elements, {})
        get_effects().add_effect(HueShift(steps_function(16, 0.2, hue)))
        #self.with_cycle(1)
        #get_effects().add_effect(BrightnessEffect(sin_start_min(0.25, 0.6)))
        self.elements.set([("peacock1","all_d")])
        get_effects().add_effect(ConstColor(color.Color(hue-0.25, 1.0, 0.9)))
        #get_effects().add_effect(HueShift(const_function(0.2)))
        #get_effects().add_effect(BrightnessEffect(sin_start_max(0.25, 0.6)))
        self.sandstorm_alternate_blink(1)
        self.with_cycle(16, 12, 16)
        self.elements.set([("peacock1","all_d")])
        #get_effects().add_effect(ConstColor(color.Color(hue -0.25, 1.0, 1.0)))
        #get_effects().add_effect(HueShift(const_function(0.0)))
        get_effects().add_effect(SnakeEffect(repeat_function(1, linear_function(1, 0)), const_function(0.6), True))
            # vocals added
        self.in_episodes(start_ep+2, start_ep+4)
        self.elements.set([("peacock1", "head")])
        get_effects().add_effect(ConstColor(color.Color(0.66, 1.0, 1.0)))
        get_effects().add_effect(BrightnessEffect(repeat_function(1, half_function(const_function(blink_min_val), const_function(1.0)))))
        self.elements.set(no_head)
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=8, start=0, end=0.5)))
        #alternate_blink(self.elements, 16)
        self.sandstorm_alternate_blink2(1)
        self.with_cycle(16, 12, 16)
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=4, start=0, end=0.35)))
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(1, 0)), const_function(0.25), True))

    def sandstorm_basic_beat3(self, start_ep):
        self.in_episodes(start_ep, start_ep+1)
        self.elements.set([wing_l_s, wing_r_s])
        hue = uniform(self.elements, {})
        self.with_cycle(8, 0, 4)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(0, 1)), const_function(0.25), True))
        self.with_cycle(16, 4, 8)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 12, 16)
        get_effects().add_effect(SnakeEffect(repeat_function(4, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 0, 12)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        self.sandstorm_alternate_blink(1)
        self.with_cycle(16, 12, 16)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=16, start=0, end=0.35)))
        alternate_blink(self.elements, 8)       
        self.in_episodes(start_ep+1, start_ep+2)
        self.elements.set([("peacock1","all")])
        hue = uniform(self.elements, {})
        get_effects().add_effect(HueShift(steps_function(16, 0.2, hue)))
        #self.with_cycle(1)
        #get_effects().add_effect(BrightnessEffect(sin_start_min(0.25, 0.6)))
        self.elements.set([("peacock1","all_d")])
        get_effects().add_effect(ConstColor(color.Color(hue-0.25, 1.0, 0.9)))
        #get_effects().add_effect(HueShift(const_function(0.2)))
        #get_effects().add_effect(BrightnessEffect(sin_start_max(0.25, 0.6)))
        self.sandstorm_alternate_blink(1)
        self.with_cycle(16, 12, 16)
        self.elements.set([("peacock1","all_d")])
        #get_effects().add_effect(ConstColor(color.Color(hue -0.25, 1.0, 1.0)))
        #get_effects().add_effect(HueShift(const_function(0.0)))
        get_effects().add_effect(SnakeEffect(repeat_function(1, linear_function(1, 0)), const_function(0.6), True))
            # vocals added
        self.in_episodes(start_ep+2, start_ep+4)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=4, start=0, end=0.8)))
        self.sandstorm_alternate_blink2(1)

    def sandstorm_minimalist(self, start_ep):
        self.in_episodes(start_ep, start_ep + 2)
        self.elements.set([("peacock1", "all")])
        uniform(self.elements, {})
        get_effects().add_effect(HueShift(steps_from_to(num_steps=4, start=0, end=0.8)))
        alternate_sin(self.elements, 16)
        # self.elements.set([("peacock1", "all")])
        # uniform(self.elements, {})
        # get_effects().add_effect(BrightnessEffect(steps_function(8, 1.0, 0.6)))
        # get_effects().add_effect(HueShift(steps_function(8, 0.1, 0.0)))
        # self.with_cycle(2)
        # #uniform(self.elements, {})
        # get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(1, 0)), const_function(0.25), True))

    def sandstorm_basic_beat2(self, start_b=0.0):
        self.in_beats(354, 368)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(0.66, 1.0, 1.0)))
        get_effects().add_effect(HueShift(linear_function(0,-0.5)))
        get_effects().add_effect(BrightnessEffect(const_function(0.9)))
        self.sandstorm_alternate_blink3(1)
    
        self.in_beats(368, 384)
        self.elements.set([wing_l_s, wing_r_s])
        hue = uniform(self.elements, {})
        self.with_cycle(8, 0, 4)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(0, 1)), const_function(0.25), True))
        self.with_cycle(16, 4, 8)
        get_effects().add_effect(SnakeEffect(repeat_function(2, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 12, 16)
        get_effects().add_effect(SnakeEffect(repeat_function(4, linear_function(1, 0)), const_function(0.25), True))
        self.with_cycle(16, 0, 12)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        self.sandstorm_alternate_blink4(1)
        self.with_cycle(16, 12, 16)
        self.elements.set([body, head, tail])
        get_effects().add_effect(ConstColor(color.Color(hue, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_from_to(num_steps=16, start=0, end=0.35)))
        alternate_blink(self.elements, 8)

    def color_section3(self, start_ep, end_ep):    
        self.in_episodes(start_ep, end_ep)
        self.elements.set([wingl, wingr])
        rainbow(self.elements, {})
        alternate_blink(self.elements, 1)
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        rainbow(self.elements, {})   
        alternate_sin(self.elements, 1)

    def color_section_beat(self, start_ep, end_ep):    
        self.in_episodes(start_ep, end_ep)
        self.elements.set([wingl, wingr])
        uniform(self.elements, {})
        alternate_blink(self.elements, 1)
        self.elements.set([("peacock1", "body"),("peacock1", "tail"), ("peacock1", "head")])
        #self.with_cycle(4)
        get_effects().add_effect(ConstColor(color.Color(0.8)))
        alternate_blink(self.elements, 1)
