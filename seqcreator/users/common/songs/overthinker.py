import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider
from seqcreator.api.color import Color
from seqcreator.api.context.energy import use_energy
from seqcreator.api.context.hue import get_primary_hue, set_hues, set_primary_hue, use_hues, use_primary_hue
from seqcreator.api.peacock_coloring import get_random_coloring, gradient, rainbow, uniform
from seqcreator.api.peacock_masking import blink_all, brightness_const, dark, fade_out, fade_out_steps, get_random_masking, hue_shift_const

import random
from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.rendering.effects.brightness import Brightness as BrightnessEffect
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.rainbow import Rainbow
from seqcreator.rendering.effects.saturation import Saturation
from seqcreator.rendering.effects.snake import SnakeEffect 
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, half_function, linear_function, repeat_function, sin_function, sin_start_max, sin_start_min, steps_from_to, steps_function

from seqcreator.segment_utils import as_symmetric

wingl = ("peacock1", "wing_l")
wingr = ("peacock1", "wing_r")
wingl_r = ("peacock1", "wing_l_r")
wingr_r = ("peacock1", "wing_r_r")
wingl_a1 = ("peacock1", "wing_l_a1")
wingl_a2 = ("peacock1", "wing_l_a2")
wingr_a1 = ("peacock1", "wing_r_a1")
wingr_a2 = ("peacock1", "wing_r_a2")
wingl_d = ("peacock1", "wing_l_d")
wingl_s = ("peacock1", "wing_l_s")
wingr_s = ("peacock1", "wing_r_s")
wings = [wingl, wingr]
wings_s = [wingl_s, wingr_s]

body = ("peacock1", "body")
body_r = ("peacock1", "body_r")
body_d = ("peacock1", "body_d")
body_a1 = ("peacock1", "body_a1")
body_a2 = ("peacock1", "body_a2")
body_s = ("peacock1", "body_s")

head = ("peacock1", "head")
head_r = ("peacock1", "head_r")
head_a1 = ("peacock1", "head_a1")
head_a2 = ("peacock1", "head_a2")
head_d = ("peacock1", "head_d")

tail = ("peacock1", "tail")
tail_r = ("peacock1", "tail_r")
tail_s = ("peacock1", "tail_s")

wing_l_s = ("peacock1", "wing_l_s")
crown = ("peacock1", "crown")
neck = ("peacock1", "neck")
neck_a1 = ("peacock1", "neck_a1")
neck_a2 = ("peacock1", "neck_a2")
all = [wingl, wingr, body, head, tail]
all_s = [wingl_s, wingr_s, body_s, head, tail_s]

all_a1 = ("peacock1", "all_a1")
all_a2 = ("peacock1", "all_a2")

class OverThinker(Song):
    def __init__(self):
        super().__init__("overthinker", 268*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        # intro 9 episodes coloring
        self.in_episodes(0, 9)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.5, 1.0, 1.0)))
        
        # episode 0 fade in
        self.in_episode(0)
        get_effects().add_effect(BrightnessEffect(linear_function(0, 0.3)))
        
        # chill intro change color every episode
        self.in_episodes(1, 9)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(8, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.with_cycle(8)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        # self.with_cycle(0.125, 0, 0.0625)
        # get_effects().add_effect(BrightnessEffect(const_function(0.9)))

        # intro, at episode 5 add small sounds
        self.in_episodes(5, 9)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(16, 0.5, 1.5)
        get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(1), True))
        # get_effects().add_effect(BrightnessEffect(sin_start_max(0.2, 1.0)))
        
        # brightness increase slightly epi 9-11
        self.in_episodes(9, 11)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.1, 1.0, 1.0)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 0.4)))
        # add beats every other beat
        self.in_episodes(9.125, 13)
        self.with_cycle(2)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        
        # more brightness increase epi 11-13
        self.in_episodes(11, 13)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.2, 1.0, 1.0)))
        # add double beats
        self.with_cycle(0.33)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # episode 11 brightness constant
        self.in_episode(11)
        get_effects().add_effect(BrightnessEffect(const_function(0.4)))
        
        # episode 12, beats 96-104
        # brightness increase beats 96-102
        self.in_beats(96, 102)
        get_effects().add_effect(BrightnessEffect(linear_function(0.4, 1)))
        # darkness for last two beats of episode 12
        self.in_beats(102, 104)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(const_function(0)))

######### START OF NOT CHILL SECTION #########
        # episodes 13-17 gradient coloring shifting every episode
        self.in_episodes(13, 17)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Rainbow(const_function(0.2), const_function(0.4)))

        self.in_episodes(13, 16.5)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(0.9), const_function(1.0)))))
        self.with_cycle(4, 1, 4)
        get_effects().add_effect(SnakeEffect(steps_from_to(3, 0, 1), const_function(0.75), True))


        # episode 13, beats 104-112
        # TODO consider what to do with this
        # self.in_beats(105.5, 108.5)
        # self.with_cycle(1)
        # get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        # self.in_beats(109.5, 110.5)
        # self.with_cycle(1)
        # get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # episode 13, last beat magic sound
        self.in_beats(111, 112)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(1), True))

        # episode 14, beats 112-120
        # rapid beats 
        self.in_beats(117.5, 117.75)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(1/16)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        self.in_beats(117.75, 119)
        self.with_cycle(1/4)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # episode 15, beats 120-128, second half fast repeats
        self.in_beats(124.66,127)
        self.elements.set(all)
        get_effects().add_effect(Rainbow(const_function(0.2), const_function(0.4)))
        get_effects().add_effect(SnakeEffect(steps_from_to(7,0,1,True), const_function(4), False))
        
        self.in_beats(127, 128)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        # episode 16, beats 128-136
        self.in_beats(130,132)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        self.in_beats(133,134.66)
        self.with_cycle(0.33)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        self.in_beats(134.66,135)
        self.with_cycle(0.0833)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # Hue shift for section 13-17 at end of section so to take on all things done in section
        self.in_episodes(13, 17)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(4, 0.1, 0)))

        # episosde 17-21 gradient coloring shifting every episode
        self.in_episodes(17, 21)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Rainbow(const_function(0.7), const_function(0.9)))
        # add beat
        self.with_cycle(2)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        
        # episode 17 beat 1 and 5 jingle sound
        self.in_episode(17)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(SnakeEffect(linear_function(0, 8), const_function(0.75), True))

        # woo woo triplets
        self.in_beats(137,139)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))
        self.in_beats(141,142)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        # 1 beat magic sound
        self.in_beats(143,144)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(0.75), True))

        # episode 18 beat 2 and 6 jingle sound
        self.in_episode(18)
        self.with_cycle(4, 1, 2)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 8), const_function(0.75), True))

        # episode 18 beat 3 woo woo snakes
        self.in_beats(146,147)
        self.elements.set(all)
        self.with_cycle(1/5)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        # episode 18 beat 7 fast beats
        self.in_beats(150,151)
        self.elements.set(all)
        self.with_cycle(1/6)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # episodes 19,20 bass every 4 beats and snakes on other 3
        self.in_episodes(19, 21)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(0.9), const_function(1.0)))))
        self.with_cycle(4, 1, 4)
        get_effects().add_effect(SnakeEffect(steps_from_to(3, 0, 1), const_function(0.75), True))

        self.in_beats(153, 155)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Rainbow(const_function(0.7), const_function(0.9)))
        self.with_cycle(1)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.5)))

        self.in_beats(155, 156)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(SnakeEffect(const_function(1), steps_from_to(3,1.5,0.5), True))

        # Hue shift for section 17-21 at end of section so to take on all things done in section
        self.in_episodes(17, 21)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(8, 0.1, 0)))

####### START NEW CHILL SECTION #######
        # episodes 21-34 chill section - alternate coloring
        self.in_episodes(21, 34)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(ConstColor(Color(0.6, 1.0, 1.0)))
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect(ConstColor(Color(0.9, 1.0, 1.0)))
        
        # episode 21 fade out to chill
        self.elements.set([("peacock1", "all")])
        self.in_episode(21)
        self.with_cycle(1/16, 0, 1/32)
        get_effects().add_effect(BrightnessEffect(const_function(0.9)))
        self.in_episodes(21, 21.25)
        get_effects().add_effect(BrightnessEffect(linear_function(0.8, 0.4)))
        self.in_episodes(21.25, 22)
        get_effects().add_effect(BrightnessEffect(linear_function(0.4, 0.2)))

        # epsiode 22-26 chill
        self.in_episodes(22, 30)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(8, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        # self.with_cycle(0.125, 0, 0.0625)
        # get_effects().add_effect(BrightnessEffect(const_function(0.9)))
        self.elements.set(all)
        self.with_cycle(8)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1.5), True))

        # episode 26-30 chill with background voice increase
        # what to add here???

        # episode 30-32 still chill but with slowly increasing beat
        self.in_episodes(30, 32)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 0.6)))
        self.in_episodes(30.125, 32)
        self.with_cycle(2)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        
        # episode 32-34 enter rapidly increasing beat
        self.in_episodes(32, 33.5)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(linear_function(0.6, 1)))
        # add double beats
        self.with_cycle(0.33)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.7, 1.0)))

        # darkness for last two beats of episode 33
        self.in_beats(268, 272)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(const_function(0)))
        self.in_beats(269.75, 271.5)
        self.elements.set([head_a1])
        get_effects().add_effect(ConstColor(Color(0.8, 0.9, 1.0)))
        self.elements.set([head_a2])
        get_effects().add_effect(ConstColor(Color(1.0, 0.9, 1.0)))

####### START NEW NOT CHILL SECTION ########
        self.in_episode(34)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(1.0, 0.9, 1.0)))

        # episode 34 special sounds no beat

        # episode 35-38 beat with some special sounds

        # episode 38-42 beat with other special sounds - different bpm section

####### START NEW CHILL SECTION #######
        # episode 42 chill
        self.in_episodes(42, 50)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.8, 1.0, 1.0)))
        self.in_episodes(42, 46)
        get_effects().add_effect(HueShift(steps_function(4, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))

        # episode 46-48 fade out
        self.in_episodes(46, 48)
        get_effects().add_effect(HueShift(steps_function(1, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.5, 0.1)))

        # episode 48-50 fade in to creshendo cut off
        self.in_episode(48)
        get_effects().add_effect(HueShift(steps_function(1, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.1, 0.3)))
        self.in_episode(49)
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 1.0)))