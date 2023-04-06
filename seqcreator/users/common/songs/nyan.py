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

class Nyan(Song):
    def __init__(self):
        super().__init__("nyan", (3 + 13/60)*60*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=8, start_offset=0)

        primary_hue = random.random()
        set_primary_hue(primary_hue)

        with use_energy(0.5):
            self.section_coloring(uniform, 0, 17)
            self.intro(0)
            self.color_section(1, 17)
            self.end_section(17)

        with use_energy(0.75):
            self.section_coloring(gradient, 17, 34)
            self.intro(17)
            self.color_section(18, 34)
            self.end_section(34)

        with use_energy(1.0):
            self.section_coloring(rainbow, 34, 51)
            self.intro(34)
            self.color_section(35, 51)
            self.end_last_section(51)

    def end_section(self, end_ep):
        timing.episodes(end_ep - 1.0, end_ep - 0.5)
        fade_out(self.elements, {})
        timing.episodes(end_ep - 0.5, end_ep)
        timing.cycle(0.125)
        blink_all(self.elements, {})

    def end_last_section(self, end_ep):
        timing.episodes(end_ep - 0.5, end_ep)
        fade_out_steps(self.elements, {})

    def color_section(self, start_ep, end_ep):
        timing.episodes(start_ep, end_ep)
        for e in range (start_ep, end_ep, 1):        
            timing.episodes(e, e+1)
            get_random_masking(self.elements, {})

    def section_coloring(self, coloring_func, start_ep, end_ep):
        timing.episodes(start_ep, end_ep)
        coloring_func(self.elements)

    def intro_single_sequence(self, episode, start_beat):
        timing.beats_in_episode(episode, 0 + start_beat, 0.25 + start_beat)
        brightness_const(0.2)
        timing.beats_in_episode(episode, 0.25 + start_beat, 0.5 + start_beat)
        brightness_const(0.35)
        timing.beats_in_episode(episode, 0.5 + start_beat, 1.0 + start_beat)
        brightness_const(0.5)

        shift_max = 0.35
        timing.beats_in_episode(episode, 0.0 + start_beat, 1.5 + start_beat)
        hue_shift_const(shift_max)

        num_steps = 10
        for step in range(0, num_steps):
            beat = 1.5 + step * 0.25
            timing.beats_in_episode(episode, start_beat + beat, start_beat + beat + 0.25)
            step_value = shift_max - step * (shift_max / num_steps)
            hue_shift_const(step_value)

    def intro(self, episode):
        g1, g2 = random.choice([[[all_a1], [all_a2]], [[wing_l, wing_r], [body, tail, head]]])
        timing.episodes(episode, episode + 0.5)
        self.elements.set(g1)
        dark(self.elements, {})

        self.elements.set(g2)
        self.intro_single_sequence(episode, 0)

        self.elements.set(g1)
        self.intro_single_sequence(episode, 4)


