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

class OverThinker(Song):
    def __init__(self):
        super().__init__("overthinker", 268*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):

        self.in_episodes(0, 23)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(Color(0.6, 1.0, 1.0)))
