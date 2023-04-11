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
        get_effects().add_effect(HueShift(steps_function(8, 0.1, 0.05)))
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.with_cycle(8)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # intro, at episode 5 add small sounds
        self.in_episodes(5, 9)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(16, 0.5, 1.5)
        get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(1), True))
        self.with_cycle(8, 1, 4)
        get_effects().add_effect(BrightnessEffect(repeat_function(3, linear_function(1.2, 1.0))))
        self.with_cycle(8, 5, 8)
        get_effects().add_effect(BrightnessEffect(repeat_function(3, linear_function(1.2, 1.0))))
        
        # brightness increase slightly epi 9-11
        self.in_episodes(9, 11)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.26, 1.0, 1.0)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 0.4)))
        
        # more brightness increase epi 11-13
        self.in_episodes(11, 13)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 1.0)))
        # add beats every other beat
        self.in_episodes(9.125, 13)
        self.with_cycle(2)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        # add double beats
        # self.with_cycle(1/4)
        # get_effects().add_effect(BrightnessEffect(sin_start_max(0.8, 1.0)))

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

        # add bass every 4 beats and moving snake on other 3 beats
        self.in_episodes(13, 16.5)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(0.9), const_function(1.0)))))
        self.with_cycle(4, 1, 4)
        get_effects().add_effect(SnakeEffect(steps_from_to(3, 0, 1), const_function(0.75), True))

        # episode 13, beats 104-112
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
        self.in_beats(132,133)
        self.with_cycle(1/16, 0, 1/32)
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))
        self.in_beats(133,134.66)
        self.with_cycle(1/3)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        self.in_beats(134.66,135)
        self.with_cycle(1/12)
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

        # episode 18 beats 144-152
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

        # episode 18 beat 4 climbing sound
        self.in_beats(147,148)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Saturation(linear_function(1, 0.5)))
        self.in_beats(148,149)
        get_effects().add_effect(BrightnessEffect(linear_function(0.4, 1.0)))

        # episode 18 beat 7, fast beats
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

        # episode 19 hold gradient coloring for 2 beats
        self.in_beats(153, 155)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Rainbow(const_function(0.7), const_function(0.9)))
        self.with_cycle(1)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.5)))

        # episode 19 beat 4 snake steps
        self.in_beats(155, 156)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(SnakeEffect(steps_from_to(3,1.5,0.5), const_function(1), True))

        # episode 19 beat 7 woo woo snakes
        self.in_beats(158,159)
        self.elements.set(all)
        self.with_cycle(1/5)
        get_effects().add_effect(SnakeEffect(linear_function(1, 0), const_function(0.5), True))

        # episode 20 beats 3-4 woo woo triplets
        self.in_beats(162,164)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))
        
        # episode 20 beats 6-7
        self.in_beats(165,166.66)
        self.with_cycle(0.33)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        self.in_beats(166.66,167)
        self.with_cycle(1/12)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))


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

        # epsiode 22-30 chill talking section
        self.in_episodes(22, 30)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(8, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(const_function(0.3)))
        self.elements.set(all)
        self.with_cycle(8)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1.5), True))

        # episode 26-27 slow fade in-out
        self.in_episodes(26, 27.5)
        self.elements.set(all)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 2.0)))

        # episode 26 talking - this is a disaster
        self.in_beats(213.5, 214.5)
        self.elements.set(all)
        self.with_cycle(1/8, 0, 1/16)
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))

        #episode 29 talking - time to wake up
        self.in_beats(238, 240)
        self.elements.set(all)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 3.0)))

        # episode 30-32 still chill but with slowly increasing beat
        self.in_episodes(30, 32)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(2, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 0.5)))
        self.in_episodes(30.125, 33.5)
        self.with_cycle(2)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        
        # episode 32-34 enter rapidly increasing beat
        self.in_episodes(32, 33.5)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(2, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.5, 1)))
        # add double beats
        # self.with_cycle(1/4)
        # get_effects().add_effect(BrightnessEffect(sin_start_max(0.8, 1.0)))

        # darkness for last two beats of episode 33
        self.in_beats(268, 272)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(const_function(0)))
        # talking - reality is
        self.in_beats(269.75, 271.5)
        self.elements.set([head_a1])
        get_effects().add_effect(ConstColor(Color(0.8, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))
        self.elements.set([head_a2])
        get_effects().add_effect(ConstColor(Color(1.0, 0.9, 1.0)))
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))
        self.elements.set([crown])
        self.with_cycle(1/8, 0, 1/16)
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))

####### START NEW NOT CHILL SECTION ########
        self.in_episodes(34, 38)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(ConstColor(Color(0.6, 1.0, 1.0)))
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect(ConstColor(Color(0.9, 1.0, 1.0)))
        
        # add bass every 4 beats and moving snake on other 3 beats
        self.in_episodes(35, 38)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(0.9), const_function(1.0)))))
        self.with_cycle(4, 1, 4)
        get_effects().add_effect(SnakeEffect(steps_from_to(3, 0, 1), const_function(0.75), True))

        # episode 34, beats 272-280
        # steps snake out, in and out again
        self.in_beats(273.66, 275)
        self.elements.set(all)
        get_effects().add_effect(SnakeEffect(const_function(1), steps_from_to(4, 1, 0.0), True))
        self.in_beats(275, 277)
        self.elements.set(all)
        get_effects().add_effect(SnakeEffect(const_function(1), steps_from_to(4, 0.0, 1), True))
        self.in_beats(277, 278.33)
        self.elements.set(all)
        get_effects().add_effect(SnakeEffect(const_function(1), steps_from_to(4, 1, 0.0), True))
        # restore everything gradually after snake out
        self.in_beats(278.33, 279)
        self.elements.set(all)
        get_effects().add_effect(BrightnessEffect(sin_start_min(0, 0.5)))
        # episode 34, last beat magic sound
        self.in_beats(279, 280)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(1), True))

        # episode 35, beats 280-288
        # sounds advance hue on a1
        self.in_beats(281.66, 283)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(ConstColor(Color(0.7, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_function(4, 0.1, 0.1)))
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect(ConstColor(Color(1.0, 1.0, 1.0)))

        # sounds advance hue on a2
        self.in_beats(285.66, 287)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(ConstColor(Color(0.2, 1.0, 1.0)))
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect(ConstColor(Color(1.0, 1.0, 1.0)))
        get_effects().add_effect(HueShift(steps_function(4, 0.1, 0.1)))

        self.in_beats(287, 287.33)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(BrightnessEffect(const_function(0)))
        self.in_beats(287.33, 287.66)
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect(BrightnessEffect(const_function(0)))

        # episode 36, beats 288-296
        self.in_beats(289,290)
        self.elements.set(all)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        self.in_beats(290,291.5)
        self.elements.set(all)
        self.with_cycle(1/2)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        self.in_beats(295,296)
        self.elements.set(all)
        get_effects().add_effect(ConstColor(Color(1.0, 1.0, 1.0)))
        get_effects().add_effect(Saturation(const_function(0.5)))
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.5)))

        # episode 37, beats 296-304
        # beats 3-4, snakes on 1/3
        self.in_beats(298,300)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        # beats 6-7, brightness on 1/3 and rapid beats at end
        self.in_beats(301,302.66)
        self.with_cycle(1/3)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        self.in_beats(302.66,303)
        self.with_cycle(0.0833)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))

        # Hue shift for section 34-38 at end of section so to take on all things done in section
        self.in_episodes(34, 38)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(4, 0.1, 0)))

##### START OF DIFFERENT BEAT SECTION, DON'T HAVE ANIMATIONS CROSS BOUNDRAIES #####
        # episosde 38-42 alternate coloring shifting every episode
        self.in_episodes(38, 42)
        self.elements.set(all)
        get_effects().add_effect(Rainbow(const_function(0), const_function(1)))
        # add beat
        self.with_cycle(2)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        
        # episode 38 beat 1 and 5 jingle sound
        self.in_episode(38)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(SnakeEffect(linear_function(0, 8), const_function(0.75), True))

        # woo woo triplets
        self.in_beats(305,307)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))
        self.in_beats(309,310)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        # # 1 beat magic sound
        self.in_beats(311,312)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(0.75), True))

        # episode 39 beat 2 and 6 jingle sound
        self.in_episode(39)
        self.with_cycle(4, 1, 2)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(SnakeEffect(linear_function(0, 8), const_function(0.75), True))

        # episode 39 beat 3 woo woo snakes
        self.in_beats(314,315)
        self.elements.set(all)
        self.with_cycle(1/5)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(1), True))

        # episode 39 beat 4 climbing sound
        self.in_beats(315,316)
        self.elements.set(all)
        get_effects().add_effect(Saturation(linear_function(1.0, 0.5)))

        # episode 39 beat 7 fast beats
        self.in_beats(318,319)
        self.elements.set(all)
        self.with_cycle(1/6)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.8, 1.0)))

        # episodes 40,41 bass every 4 beats and snakes on other 3
        self.in_episodes(40, 42)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(BrightnessEffect(repeat_function(8, half_function(const_function(0.9), const_function(1.0)))))
        self.with_cycle(4, 1, 4)
        get_effects().add_effect(SnakeEffect(steps_from_to(3, 0, 1), const_function(0.75), True))

        # self.in_beats(321, 323)
        self.elements.set(all)
        get_effects().add_effect(Rainbow(const_function(0), const_function(1)))
        self.with_cycle(1)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.5)))

        # episode 40 beat 4 snake steps
        self.in_beats(323, 324)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(SnakeEffect(const_function(1), steps_from_to(3,1.5,0.5), True))

        # episode 40 beat 7 woo woo snakes
        self.in_beats(326,327)
        self.elements.set(all)
        self.with_cycle(1/5)
        get_effects().add_effect(SnakeEffect(linear_function(1, 0), const_function(0.5), True))

        # episode 41 beats 3-4 woo woo triplets
        self.in_beats(330,331)
        self.elements.set(all)
        self.with_cycle(1/3)
        get_effects().add_effect(SnakeEffect(linear_function(1, 0), const_function(0.5), True))

        # episode 41 beats 6-7, brightness on 1/3 and rapid beats at end
        self.in_beats(333,334.66)
        self.with_cycle(1/3)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))
        self.in_beats(334.66,335)
        self.with_cycle(1/12)
        get_effects().add_effect(BrightnessEffect(sin_start_max(0.5, 1.0)))


        # Hue shift for section 38-42 at end of section so to take on all things done in section
        self.in_episodes(38, 42)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(HueShift(steps_function(8, 0.1, 0)))

####### START NEW CHILL SECTION #######
        # episode 42 chill
        self.in_episodes(42, 46)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(Rainbow(const_function(0.2), const_function(0.7)))
        get_effects().add_effect(SnakeEffect(linear_function(2.5,1.0),const_function(0.75), True))
        get_effects().add_effect(HueShift(steps_function(4, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(const_function(0.25)))

        # episode 42 fade down to 0.25
        self.in_episode(42)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.3)))

        self.elements.set([head])
        # talking - i'm not trying to put you down
        self.in_beats(340.5, 342)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 2.0)))
        # talking - expression of you as you are
        self.in_beats(346.5, 349.5)
        self.with_cycle(1)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 2.0)))
        # talking - one must live
        self.in_beats(352.5, 354)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 2.0)))
        # talking - we need to survive
        self.in_beats(357, 359)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 2.0)))
        # talking - to go on
        self.in_beats(360.5, 361.5)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 2.0)))
        # talking - we must go on
        self.in_beats(364.5, 366)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 3.0)))
        # keep brightness high for 2 beats
        self.in_beats(366, 368)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(const_function(3.0)))

        # episode 46-48 fade out
        self.in_episodes(46, 47)
        self.elements.set([("peacock1", "all_d")])
        get_effects().add_effect(Rainbow(const_function(0), const_function(1)))
        get_effects().add_effect(HueShift(steps_function(1, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.9, 0.1)))
        get_effects().add_effect(Saturation(linear_function(1.0, 0.2)))

        # episode 47-49 fade in to creshendo cut off
        self.in_episodes(47, 49)
        self.elements.set(all_s)
        get_effects().add_effect(Rainbow(const_function(0), const_function(1)))
        get_effects().add_effect(SnakeEffect(linear_function(0.0,1.0),const_function(1.0), False))
        get_effects().add_effect(HueShift(steps_function(1, 0.1, 0.0625)))
        get_effects().add_effect(BrightnessEffect(linear_function(0.1, 0.3)))
        get_effects().add_effect(Saturation(linear_function(0.2, 1.0)))

        self.in_episode(49)
        self.elements.set(all_s)
        get_effects().add_effect(Rainbow(const_function(0), const_function(1)))
        get_effects().add_effect(SnakeEffect(linear_function(1.0,2.0),const_function(1.0), True))
        get_effects().add_effect(BrightnessEffect(linear_function(0.3, 1.0)))
        get_effects().add_effect(Saturation(linear_function(1.0, 0.2)))