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
from seqcreator.rendering.functions.functions_store import const_function, half_function, linear_function, sin_function, sin_start_mid_down, sin_start_min, sin_start_max, sin_start_mid_up, steps_from_to, repeat_function

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
wingr_d = ("peacock1", "wing_r_d")
wingl_s = ("peacock1", "wing_l_s")
wingr_s = ("peacock1", "wing_r_s")
wings = [wingl, wingr]
wings_s = [wingl_s, wingr_s]
wings_d = [wingl_d, wingr_d]

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
tail_a1 = ("peacock1", "tail_a1")
tail_a2 = ("peacock1", "tail_a2")
tail_d = ("peacock1", "tail_d")

wing_l_s = ("peacock1", "wing_l_s")
crown = ("peacock1", "crown")
neck = ("peacock1", "neck")
neck_a1 = ("peacock1", "neck_a1")
neck_a2 = ("peacock1", "neck_a2")

all = [wingl, wingr, body, head, tail]
all_s = [wingl_s, wingr_s, body_s, head, tail_s]
all_a1 = [wingl_a1, wingr_a1, body_a1, head_a1, tail_a1]
all_a2 = [wingl_a2, wingr_a2, body_a2, head_a2, tail_a2]
all_d = [wingl_d, wingr_d, body_d, head_d, tail_d]

# colorful

_colorful_crazy_rounds = 32
def colorful_mild(): return Rainbow(const_function(0.0), const_function(1.0))


def colorful_crazy(): return Rainbow(const_function(0.0),
                                     const_function(_colorful_crazy_rounds))


def colorful_increasing(rel_start, num_steps): return Rainbow(const_function(
    0.0), steps_from_to(num_steps=num_steps, start=rel_start * _colorful_crazy_rounds, end=_colorful_crazy_rounds, on_end = True))


# red
_red_hue = 0.33
def color_red(brightness=1, saturation=1): return ConstColor(
    Color(_red_hue, saturation, brightness))


color_red_increase_intensity = [
    lambda: color_red(0.125, 0.6),
    lambda: color_red(0.5, 0.9),
    lambda: color_red(0.75, 1.0),
]
def color_black(): return ConstColor(Color(0.0, 0.0, 0.0))
def color_white(brightness=1): return ConstColor(Color(0.0, 0.0, brightness))
def gradinet_reds(): return Rainbow(const_function(_red_hue - 0.0), const_function(_red_hue + 0.05))

class Req(Song):
    def __init__(self):
        super().__init__("req", 300*1000, 0)
        self.elements = element_provider.get_element_provider()

    def introducing_max_colorful(self):
        # expecting time frame
        self.elements.set([("peacock1", "all")])
        # first long note
        self.with_cycle(16, 0, 0.5)
        get_effects().add_effect(colorful_crazy())
        self.with_cycle(16, 8, 8.25)
        get_effects().add_effect(colorful_crazy())
        # short notes
        for [cycle_beat_start, cycle_beat_end] in [[1.5, 1.75], [2.0, 2.25], [3.5, 3.75], [4, 4.25]]:
            self.with_cycle(8, cycle_beat_start, cycle_beat_end)
            get_effects().add_effect(colorful_crazy())

        # changes notes
        self.with_cycle(8, 5.5, 8)
        get_effects().add_effect(colorful_increasing(0.0, 10))

    def happy_mild(self):
        # expecting time frame
        self.with_cycle(2)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect((BrightnessEffect(sin_start_min(0.5, 1.0))))
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect((BrightnessEffect(sin_start_max(0.5, 1.0))))

        self.elements.set([("peacock1", "all")])
        self.with_cycle(1, 0, 1)
        get_effects().add_effect((BrightnessEffect(linear_function(0.75, 1.0))))
        self.with_cycle(16, 8, 12)
        get_effects().add_effect((HueShift(const_function(0.25))))
        self.with_cycle(16, 12, 16)
        get_effects().add_effect((HueShift(const_function(0.5))))

    def animation_bad_vibez_1_coloring(self, bad_vibez_start_episode: int):
        # coloring of section.
        # first 2 episodes are colorful and next 2 are red
        self.in_episodes(bad_vibez_start_episode, bad_vibez_start_episode + 2)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(colorful_crazy())
        self.in_episodes(bad_vibez_start_episode + 2, bad_vibez_start_episode + 4)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(8, 0, 4)
        get_effects().add_effect(color_red_increase_intensity[0]())
        self.with_cycle(8, 4, 6)
        get_effects().add_effect(color_red_increase_intensity[1]())
        self.with_cycle(8, 6, 8)
        get_effects().add_effect(color_red_increase_intensity[2]())

    def animation_bad_vibez_1_snakes(self, bad_vibez_start_episode: int):

        cycle = 1
        snake_length = 0.5

        # first 2 episodes starts with snakes with moderate speed
        self.in_episodes(bad_vibez_start_episode, bad_vibez_start_episode + 2)
        self.with_cycle(cycle)
        self.elements.set(all_s)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(snake_length), True))

        # add confetti on snakes in first 2 episodes
        self.in_episodes(bad_vibez_start_episode, bad_vibez_start_episode + 2)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(cycle / 4)
        get_effects().add_effect(SnakeEffect(
            linear_function(0.0, 1.0), const_function(0.75), True))

        # 3rd episode snakes become shorter to make it more dark and intense
        self.in_episode(bad_vibez_start_episode + 2)
        self.with_cycle(cycle)
        self.elements.set(all_s)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(snake_length / 2), True))

    def animation_bad_vibez_2_snakes(self, bad_vibez_start_episode: int):

        cycle = 4
        snake_length = 1.0

        # first episode snake
        self.in_episodes(bad_vibez_start_episode, bad_vibez_start_episode + 1)
        self.with_cycle(cycle)
        self.elements.set(all_s)
        get_effects().add_effect(SnakeEffect(linear_function(0, 1), const_function(snake_length), True))

        # second espisode confetti
        self.in_episodes(bad_vibez_start_episode + 1, bad_vibez_start_episode + 2)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(cycle / 4)
        get_effects().add_effect(SnakeEffect(
            linear_function(0.0, 1.0), const_function(0.75), True))

    def animation_bad_vibez_headace(self, bad_vibez_start_episode: int):
        # first section is headace free
        # next 3 out of 4 episodes intdoce a headace coloring overlay
        # that captures a background vocal level of red in increasing intensity
        self.in_episodes(bad_vibez_start_episode + 1, bad_vibez_start_episode + 4)
        self.elements.set([("peacock1", "head")])
        # 4 beats min intensity
        self.with_cycle(8, 0, 4)
        get_effects().add_effect(color_red_increase_intensity[0]())
        # 2 beats mid intensity
        self.with_cycle(8, 4, 6)
        get_effects().add_effect(color_red_increase_intensity[1]())
        # 2 beats max intensity
        self.with_cycle(8, 6, 8)
        get_effects().add_effect(color_red_increase_intensity[2]())
        
        # general beat on head to make it more red
        self.with_cycle(1, 0, 0.0625)
        get_effects().add_effect(color_red())

    def coloring_bad_vibez_1_drums(self):
        """
        when a bad vibez drum kiks in, this will flash as the drum color
        """
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(color_white(0.5))
        self.elements.set([("peacock1", "head")])
        get_effects().add_effect(color_red())

    def coloring_bad_vibez_2_drums(self):
        """
        when a bad vibez drum kiks in, this will flash as the drum color
        """
        self.elements.set([("peacock1", "all_d")])
        get_effects().add_effect(color_red())

    def effect_bad_vibez_drum_blink(self):
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(repeat_function(
            8, half_function(const_function(0.0), const_function(1.0)))))

    def animation_bad_vibez_1_drums(self, bad_vibez_start_episode: int):
        # there are 2 kinds of drums in each 8 beats:
        # both flash a quick white and red on the peacock that accompanies the drums

        # first drum in quicker (0.25 beats) and less intense.
        # it is not present in the first episode (starts once the headace kiks in)
        self.in_episodes(bad_vibez_start_episode + 1, bad_vibez_start_episode + 3)
        self.with_cycle(8, 3.75, 4)
        self.coloring_bad_vibez_1_drums()
        self.effect_bad_vibez_drum_blink()
        
        # second drum in 8 beats lasts longer (0.5 beats) and is more intense
        # it spans the entire bad vibez section from beginning, but last occurence is disabled due to intro to max intensity section
        self.in_episodes(bad_vibez_start_episode + 0, bad_vibez_start_episode + 3.5)
        self.with_cycle(8, 7.5, 8)
        self.coloring_bad_vibez_1_drums()
        self.effect_bad_vibez_drum_blink()

    def animation_bad_vibez_2_drums(self, bad_vibez_start_episode: int):
        # second drum in 8 beats lasts longer (0.5 beats) and is more intense
        # it spans the entire bad vibez section from beginning, but last occurence is disabled due to intro to max intensity section
        self.in_episodes(bad_vibez_start_episode + 0, bad_vibez_start_episode + 1)
        self.with_cycle(8, 7.5, 8)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(color_red())
        self.in_episodes(bad_vibez_start_episode + 1, bad_vibez_start_episode + 2.5)
        self.with_cycle(8, 7.5, 8)
        self.elements.set([("peacock1", "all_d")])
        get_effects().add_effect(color_red())
        
        self.in_episodes(bad_vibez_start_episode + 0, bad_vibez_start_episode + 2.5)
        self.with_cycle(8, 7.5, 8)
        self.effect_bad_vibez_drum_blink()

    def animation_bad_vibez_trumble(self):
        self.elements.set([("peacock1", "all")])
        tumble_cycle = 1.0 / 16.0
        low_intensity_rel_time = 0.25
        low_intensity_brightness = 0.8
        self.with_cycle(tumble_cycle, 0, tumble_cycle * low_intensity_rel_time)
        get_effects().add_effect(BrightnessEffect(const_function(low_intensity_brightness)))

    def effect_bad_vibez_end_drums(self):
        """
        low intensity drums that are shifting out from this section and into the next max intensisty section
        """

        # turn off everything but leave crown on with red
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(color_black())
        self.elements.set([("peacock1", "crown")])
        get_effects().add_effect(color_red())

        # set the crawn to blink black on those beats
        self.with_cycle(0.25, 0, 0.0625)
        get_effects().add_effect(color_black())

    def section_happy_intro(self):
        """
        This is the section at begining where everything is colorful ang joyful.
        There is no yet any red or drama.
        It spans episodes 0-8.
        The background is colorful but not too much (0-1) spread accross the entire element
        """

        # This will be the color across the section, unless overriden by other color
        self.in_episodes(0, 8)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(colorful_mild())

        # make mild hue shift on every note at 2 first episodes
        # everything is good
        self.in_episodes(0, 2)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(4)
        get_effects().add_effect(HueShift(steps_from_to(num_steps=8, start=0, end=0.25)))
        self.elements.set(wings)
        get_effects().add_effect(HueShift(steps_from_to(num_steps=8, start=0, end=0.25, on_end=True)))

        self.in_episode(0)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))

        self.in_episode(1)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(HueShift(const_function(0.125)))

        self.in_episodes(2, 4)
        self.happy_mild()

        self.in_episode(3)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect(HueShift(const_function(0.125)))

        # introducing coloful max
        self.in_episodes(4, 6)
        self.introducing_max_colorful()

        self.in_episodes(6, 7)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(2)
        get_effects().add_effect(HueShift(sin_start_mid_up(-0.25, 0.25)))
        self.with_cycle(4, 0, 1)
        get_effects().add_effect(Saturation(linear_function(0.0, 1.0)))

        self.in_episodes(7, 8)
        self.happy_mild()

    def section_bad_vibez_1(self):
        """
        This is the section where things are starting to shift from good (colorful) to bad (red).
        It spans episodes 8-12.
        """

        self.animation_bad_vibez_1_coloring(8)

        self.animation_bad_vibez_1_snakes(8)
        self.animation_bad_vibez_headace(8)
        self.animation_bad_vibez_1_drums(8)

        self.in_episode(11)
        self.animation_bad_vibez_trumble()

        self.in_beats(191, 192)
        self.effect_bad_vibez_end_drums()

    def section_bad_vibez_2(self):
        """
        This is the second section where things are dark and bad.
        It starts after max intensity drama section and is followed by one as well.
        It spans episodes 15-18.
        """

        self.in_episodes(15, 18)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(colorful_mild())
        self.with_cycle(2)
        get_effects().add_effect(Saturation(sin_start_max(0.75, 1.0)))
        self.in_episodes(15, 17)
        get_effects().add_effect(BrightnessEffect(const_function(0.25)))
        self.in_episodes(17, 18)
        self.animation_bad_vibez_trumble()
        self.in_episodes(17, 18)
        self.elements.set([("peacock1", "crown")])
        get_effects().add_effect(ConstColor(Color(0.0, 1.0, 1.0)))

        self.elements.set([("peacock1", "all")])
        self.in_beats(272, 276)
        get_effects().add_effect(BrightnessEffect(const_function(0.25)))
        self.in_beats(276, 276.5)
        get_effects().add_effect(BrightnessEffect(linear_function(0.25, 0.4)))
        self.in_beats(276.5, 278)
        get_effects().add_effect(BrightnessEffect(const_function(0.4)))
        self.in_beats(278, 278.5)
        get_effects().add_effect(BrightnessEffect(linear_function(0.4, 0.65)))
        self.in_beats(278.5, 284)
        get_effects().add_effect(BrightnessEffect(const_function(0.65)))
        self.in_beats(284, 284.5)
        get_effects().add_effect(BrightnessEffect(linear_function(0.65, 1.0)))

        self.animation_bad_vibez_2_snakes(15)
        # self.animation_bad_vibez_headace(15)
        self.animation_bad_vibez_2_drums(15)

        self.in_beats(285.75, 286.75)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(steps_from_to(4, 1, 0.25)))

        self.in_beats(286.75, 288)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(const_function(0.25)))

        self.in_beats(286.75, 288)
        self.elements.set([body])
        get_effects().add_effect(BrightnessEffect(const_function(0.0)))
        self.in_beats(287, 288)
        self.elements.set(wings)
        get_effects().add_effect(BrightnessEffect(const_function(0.0)))
        self.in_beats(287.25, 288)
        self.elements.set([tail])
        get_effects().add_effect(BrightnessEffect(const_function(0.0)))
        self.in_beats(287.5, 288)
        self.elements.set([neck])
        get_effects().add_effect(BrightnessEffect(const_function(0.0)))
        self.in_beats(287.75, 288)
        self.elements.set([crown])
        get_effects().add_effect(BrightnessEffect(steps_from_to(5, 1.0, 0.0)))

    def section_drama_1(self):
        """
        This section is the max intensity in the song.
        It spans episodes 12-15.
        Everything is max energy drama and intensity.
        """

        # coloring of section. red unless overriden
        self.in_episodes(12, 15)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(color_red())

        self.in_episodes(12, 14)
        # this adds the drama notes, two notes, quite, two notes
        notes = self.trigger_config["notes"]

        drama_notes = next(n for n in notes if n["name"] == "drama-alternate")
        cycle_total_beats = drama_notes["cycleTotalBeats"]
        for note in drama_notes["notes"]:
            note_start_beat = note["startBeat"]
            note_end_beat = note_start_beat + note["lengthBeats"]
            self.with_cycle(cycle_total_beats, note_start_beat, note_end_beat)
            get_effects().add_effect(colorful_crazy())

        drama_buildup = next(n for n in notes if n["name"] == "drama-buildup")
        cycle_total_beats = drama_buildup["cycleTotalBeats"]

        # fast snake on the body on the drama buildup part
        self.with_cycle(cycle_total_beats, 5.5, 8)
        self.elements.set([wingl, wingr])
        get_effects().add_effect(SnakeEffect(linear_function(0, 20), const_function(0.50), True))

        # cover head with something different on drama buildup part
        self.with_cycle(cycle_total_beats, 5.5, 8)
        self.elements.set([head])
        get_effects().add_effect(color_red(0.5))
        self.elements.set([head])
        get_effects().add_effect(Rainbow(const_function(0.0), const_function(4.0)))
        get_effects().add_effect(HueShift(steps_from_to(10, 0, 1, True)))

        # drums every 8 beats as white explosion
        self.with_cycle(8, 0, 1)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Saturation(linear_function(0.0, 1.0)))

        self.in_beats(224, 236)
        self.elements.set(all)
        self.with_cycle(2)
        get_effects().add_effect(SnakeEffect(sin_start_mid_up(0.0, 1.0), sin_start_max(1.0, 0.25), False))
        self.in_beats(232, 236)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(2, 0, 1)
        get_effects().add_effect(Saturation(linear_function(0.75, 1.0)))
        self.in_beats(236, 237)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(linear_function(0.0, 1.0)))
        # self.elements.set([("peacock1", "all_a1")])
        # self.with_cycle(1, 0, 1)
        # get_effects().add_effect(color_black())
        # self.elements.set([("peacock1", "all_a2")])
        # self.with_cycle(1, 0.5, 1)
        # get_effects().add_effect(color_black())

        # turn off elements at section end
        self.in_beats(238, 240)
        self.elements.set([head])
        get_effects().add_effect(color_black())

        self.in_beats(238.5, 240)
        self.elements.set([wingl, wingr])
        get_effects().add_effect(color_black())

        self.in_beats(239, 240)
        self.elements.set([tail])
        get_effects().add_effect(color_black())

        self.in_beats(239.5, 240)
        self.elements.set([body])
        get_effects().add_effect(color_black())

    def section_drama_2(self):

        # coloring of section. red except dots unless overriden
        self.in_episodes(18, 19)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(gradinet_reds())
        self.in_episodes(19, 22)
        self.elements.set([("peacock1", "all_r")])
        get_effects().add_effect(color_red())
        self.in_episodes(18, 20)
        self.with_cycle(1)
        get_effects().add_effect(SnakeEffect(steps_from_to(16, 0, 1), const_function(1), True))
        self.in_episodes(20, 22)
        self.with_cycle(1)
        get_effects().add_effect(SnakeEffect(linear_function(0, 0.5), const_function(1), True))

        self.in_episodes(18, 20)
        # this adds the drama notes, two notes, quite, two notes
        notes = self.trigger_config["notes"]

        drama_notes = next(n for n in notes if n["name"] == "drama-alternate")
        cycle_total_beats = drama_notes["cycleTotalBeats"]
        for note in drama_notes["notes"]:
            note_start_beat = note["startBeat"]
            note_end_beat = note_start_beat + note["lengthBeats"]
            self.with_cycle(cycle_total_beats, note_start_beat, note_end_beat)
            self.elements.set([("peacock1", "all")])
            get_effects().add_effect(color_black())
            self.elements.set([("peacock1", "all_d")])
            get_effects().add_effect(colorful_crazy())

        self.in_episodes(18, 20)
        # notes alternating x10 as dim colors on wings / rest
        self.with_cycle(cycle_total_beats, 5.5, 8)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(color_black())
        self.elements.set([("peacock1", "all_d")])
        get_effects().add_effect(colorful_crazy())

        self.in_episodes(18, 19)
        self.with_cycle(cycle_total_beats, 5.5, 8)
        self.elements.set([head])
        get_effects().add_effect(BrightnessEffect(repeat_function(5, half_function(const_function(1), const_function(0)))))
        self.elements.set([wingl, wingr, tail, body])
        get_effects().add_effect(BrightnessEffect(repeat_function(5, half_function(const_function(0), const_function(1)))))

        self.in_episodes(19, 20)
        self.with_cycle(cycle_total_beats, 5.5, 8)
        self.elements.set([head, tail, body])
        get_effects().add_effect(Saturation(repeat_function(5, half_function(const_function(1), const_function(0.5)))))
        self.elements.set(wings)
        get_effects().add_effect(Saturation(repeat_function(5, half_function(const_function(0.5), const_function(1)))))

        # blend a lot of red with dotted colorful
        self.in_episodes(20, 22)

        # coloring, # beat of each 4
        self.in_episodes(20, 22)
        self.with_cycle(4, 0, 1)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.0)))

        # remaining 3 beats #1-#4 of each 4
        self.in_episodes(20, 22)
        self.elements.set([("peacock1", "all")])
        self.with_cycle(4, 1, 4)
        get_effects().add_effect(BrightnessEffect(const_function(0.5)))
        get_effects().add_effect(Saturation(const_function(0.5)))
        # self.elements.set(all)
        # self.with_cycle(2)
        # get_effects().add_effect(SnakeEffect(sin_start_max(0, 0.5), const_function(1.75), True))

        # very cool effect
        self.in_episodes(20, 21)
        for idx, segment in enumerate(all_d):
            self.elements.set([segment])
            self.with_cycle(4)
            get_effects().add_effect(color_red())
            self.with_cycle(4, 1, 4)
            hue_shift_amount = (idx + 1) * 0.3
            get_effects().add_effect(HueShift(linear_function(0.0, hue_shift_amount)))

        self.in_episodes(21, 22)
        for idx, segment in enumerate(all_d):
            self.elements.set([segment])
            self.in_episodes(21, 22)
            get_effects().add_effect(color_red())
            self.with_cycle(1)
            get_effects().add_effect(BrightnessEffect(sin_start_mid_up(0.0, 1.0)))

        # drums every 8 beats as white explosion
        self.in_episodes(18, 22)
        self.with_cycle(8, 0, 1)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Saturation(linear_function(0.0, 1.0)))

        self.elements.set([body])
        self.in_beats(350, 353)
        get_effects().add_effect(color_red())

        self.elements.set([tail])
        self.in_beats(350.5, 353)
        get_effects().add_effect(color_red())

        self.elements.set(wings)
        self.in_beats(351, 353)
        get_effects().add_effect(color_red())

        self.elements.set([head])
        self.in_beats(351.5, 353)
        get_effects().add_effect(color_red())

        self.in_beats(352, 353)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.0)))



    def render_effects(self):
        self.section_happy_intro()
        self.section_bad_vibez_1()
        self.section_drama_1()
        self.section_bad_vibez_2()
        self.section_drama_2()

