import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.api.peacock_coloring import get_random_coloring
from seqcreator.api.peacock_masking import get_random_masking

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

class Nyan(Song):
    def __init__(self):
        super().__init__("nyan", (3 + 13/60)*60*1000, 0)
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
        timing.song_settings(bpm=128, beats_per_episode=8, start_offset=0)

        self.color_section(1, 17)
        self.color_section(18, 34)
        self.color_section(35, 51)

    def color_section(self, start_ep, end_ep):
        [hue1, hue2] = self.get_hues()        
        timing.episodes(start_ep, end_ep)
        get_random_coloring(self.elements, {'hue': hue1, 'hue2': hue2, 'intensity': 0.25})
        for e in range (start_ep, end_ep, 1):        
            timing.episodes(e, e+1)
            get_random_masking(self.elements, {})        

