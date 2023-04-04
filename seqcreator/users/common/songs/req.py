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
from seqcreator.rendering.functions.functions_store import const_function, half_function, linear_function, sin_function, steps_function

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

wing_l_s = ("peacock1", "wing_l_s")
crown = ("peacock1", "crown")
neck = ("peacock1", "neck")
neck_a1 = ("peacock1", "neck_a1")
neck_a2 = ("peacock1", "neck_a2")
all = [wingl, wingr, body, head, tail]

all_a1 = ("peacock1", "all_a1")
all_a2 = ("peacock1", "all_a2")

class Req(Song):
    def __init__(self):
        super().__init__("req", 300*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=60, beats_per_episode=60, start_offset=0)

        self.in_episodes(0, 23)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.6, 1.0, 1.0)))

        self.in_episodes(0, 2)
        self.elements.set([("peacock1", "all")])
        # notes in intro
        # self.with_cycle(4)
        # get_effects().add_effect((HueShift(steps_function(8, 0.125 / 8, -(0.125 / 8) / 2))))
        # self.with_cycle(1)
        # get_effects().add_effect((BrightnessEffect(sin_function(1.0, 0.5, 0.25, 1))))

        self.in_episodes(2, 4)
        self.with_cycle(8)
        self.elements.set([("peacock1", "all_a1")])
        get_effects().add_effect((BrightnessEffect(sin_function(0.25, 1.0, -0.25, 1))))
        self.elements.set([("peacock1", "all_a2")])
        get_effects().add_effect((BrightnessEffect(sin_function(0.25, 1.0, 0.25, 1))))

        self.elements.set([("peacock1", "all")])
        self.in_episodes(2, 4)
        self.with_cycle(1, 0, 1)
        get_effects().add_effect((BrightnessEffect(linear_function(0.5, 1.0))))
        self.with_cycle(16, 8, 12)
        get_effects().add_effect((HueShift(const_function(0.25))))
        self.with_cycle(16, 12, 16)
        get_effects().add_effect((HueShift(const_function(0.125))))

        # starting to get bad
        self.in_episodes(8, 10)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Rainbow(const_function(0.0), const_function(32.0)))
        self.in_episodes(10, 12)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 0.25)))

        # snakes
        self.in_episodes(8, 10)
        self.with_cycle(1)
        for elem in all:
            self.elements.set([elem])
            rand_start = random.random()
            get_effects().add_effect(SnakeEffect(linear_function(rand_start, rand_start + 1), const_function(0.5), True))
        self.in_episodes(10, 11)
        self.with_cycle(1.0)
        for elem in all:
            self.elements.set([elem])
            rand_start = random.random()
            get_effects().add_effect(SnakeEffect(linear_function(rand_start, rand_start + 1), const_function(0.25), True))
        self.in_episodes(8, 10)
        self.elements.set([("peacock1", "all_r")])
        self.with_cycle(0.25)
        get_effects().add_effect(SnakeEffect(linear_function(0.0, 1.0), const_function(0.75), True))

        # headace
        self.in_episodes(9,12)
        self.elements.set([("peacock1", "head")])
        get_effects().add_effect(ConstColor(Color(0.33, 0.9, 0.25)))
        self.with_cycle(1, 0, 0.0625)
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 1.0)))
        self.with_cycle(1, 0, 0.0625)
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 1.0)))
        self.with_cycle(8, 7.5, 8)
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 1.0)))

        # drums introducing max intancity section in song
        self.in_beats(191, 192)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.0, 0.0, 0.0)))
        self.elements.set([("peacock1", "crown")])
        get_effects().add_effect(ConstColor(Color(0.0, 1.0, 1.0)))
        self.with_cycle(0.25, 0.125, 0.25)
        get_effects().add_effect(ConstColor(Color(0.0, 0.0, 0.0)))

        # max intensity section
        self.in_episodes(12, 15)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 1.0)))

        notes = self.trigger_config["notes"]

        drama_notes = next(n for n in notes if n["name"] == "drama-alternate")
        cycle_total_beats = drama_notes["cycleTotalBeats"]
        for note in drama_notes["notes"]:
            note_start_beat = note["startBeat"]
            note_end_beat = note_start_beat + note["lengthBeats"]
            self.with_cycle(cycle_total_beats, note_start_beat, note_end_beat)
            get_effects().add_effect(Rainbow(const_function(0.0), const_function(32.0)))

        drama_buildup = next(n for n in notes if n["name"] == "drama-buildup")
        cycle_total_beats = drama_buildup["cycleTotalBeats"]

        self.with_cycle(cycle_total_beats, 5.5, 8)
        self.elements.set([head])
        get_effects().add_effect(ConstColor(Color(0.33, 1.0, 0.5)))
        self.elements.set([head_a1])
        get_effects().add_effect(Rainbow(const_function(0.0), const_function(4.0)))
        get_effects().add_effect(HueShift(steps_function(10, 0.1, 0.0)))
        # self.elements.set([head_a2])
        # get_effects().add_effect(ConstColor(Color(0.0, 0.0, 0.0)))

        # self.elements.set([head])
        # for note_i in range(0, 5):
        #     note = drama_buildup["notes"][note_i]

        #     note_start_beat = note["startBeat"]
        #     note_end_beat = note_start_beat + note["lengthBeats"]
        #     self.with_cycle(cycle_total_beats, note_start_beat, note_end_beat)
            # self.elements.set([[all_a1], [all_a2]][0])
            # get_effects().add_effect(Rainbow(const_function(0 + 0.25 * note_i), const_function(32)))
            # get_effects().add_effect(ConstColor(Color(0.1 + note_i * 0.1, 0.8, 1.0)))
            # self.with_cycle(cycle_total_beats, note_end_beat, note_end_beat + note["lengthBeats"])
            # get_effects().add_effect(ConstColor(Color(0.15 + note_i * 0.1, 0.8, 1.0)))

        self.with_cycle(8, 0, 1)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(Saturation(linear_function(0.0, 1.0)))


        self.elements.set([("peacock1", "all")])
        self.in_episode(17)
        self.with_cycle(1, 0.0, 0.125)
        get_effects().add_effect((BrightnessEffect(linear_function(4.0, 1.0))))
