import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.api.context.energy import use_energy
from seqcreator.api.context.hue import get_primary_hue, set_hues, set_primary_hue, use_hues, use_primary_hue
from seqcreator.api.peacock_coloring import get_random_coloring, gradient, rainbow, uniform
from seqcreator.api.peacock_masking import blink_all, brightness_const, dark, fade_out, fade_out_steps, get_random_masking, hue_shift_const

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
crown = ("peacock1", "crown")
neck = ("peacock1", "neck")
neck_a1 = ("peacock1", "neck_a1")
neck_a2 = ("peacock1", "neck_a2")
all = [wingl, wingr, body, head, tail]

all_a1 = ("peacock1", "all_a1")
all_a2 = ("peacock1", "all_a2")

class Peacock(Song):
    def __init__(self):
        super().__init__("peacock", 300*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=60, beats_per_episode=60, start_offset=0)

        self.paint_peacock_sounds(4)
        self.paint_peacock_sounds(40)
        self.paint_peacock_sounds(50)
        self.paint_peacock_sounds(90)
        self.paint_peacock_sounds(130)
        self.paint_peacock_sounds(138)
        self.paint_peacock_sounds(155)

    def paint_peacock_sounds(self, start_time: float):

        timing.beats(start_time, start_time + 4.5)
        gradient(self.elements)
