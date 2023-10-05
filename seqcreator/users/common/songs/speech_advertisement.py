import config
from seqcreator.animations.song import Song
from seqcreator.api import element_provider, color
from seqcreator.api.context.energy import use_energy
from seqcreator.api.context.hue import get_primary_hue, set_hues, set_primary_hue, use_hues, use_primary_hue
from seqcreator.api.peacock_coloring import get_random_coloring, gradient, rainbow, uniform
from seqcreator.api.peacock_masking import blink_all, brightness_const, dark, fade_out, fade_out_steps, get_random_masking, hue_shift_const

from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.rendering.effects.brightness import Brightness as BrightnessEffect
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.saturation import Saturation
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import linear_function, sin_start_max, sin_start_min

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

class SpeechAdvertisement(Song):
    def __init__(self):
        super().__init__("speech_advertisement", 180*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):

        self.in_minutes_seconds(0, 0, 4, 0)
        self.elements.set([("peacock1", "all")])
        get_effects().add_effect(ConstColor(color.Color(0.6, 0.75, 0.125)))
        self.elements.set([("peacock1", "all_d")])
        get_effects().add_effect(ConstColor(color.Color(0.6, 1.0, 1.0)))

        self.paint_peacock_sounds(0, 4)
        self.paint_peacock_sounds(0, 40)
        self.paint_peacock_sounds(0, 50)
        self.paint_peacock_sounds(1, 30)
        self.paint_peacock_sounds(2, 10)
        self.paint_peacock_sounds(2, 18)
        self.paint_peacock_sounds(2, 35)

    def paint_peacock_sounds(self, start_minute: float, start_second: float):

        self.in_minutes_seconds(start_minute, start_second, start_minute, start_second + 4.5)
        self.elements.set([("peacock1", "all")])

        # coloring
        get_effects().add_effect(ConstColor(color.Color(0.6, 1.0, 0.25)))

        # fade out background
        self.in_minutes_seconds(start_minute, start_second - 0.25, start_minute, start_second)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.0)))
        # fade in noise
        self.in_minutes_seconds(start_minute, start_second, start_minute, start_second + 0.25)
        get_effects().add_effect(BrightnessEffect(linear_function(0.0, 1.0)))
        # fade out noise
        self.in_minutes_seconds(start_minute, start_second + 4.5 - 0.25, start_minute, start_second + 4.5)
        get_effects().add_effect(BrightnessEffect(linear_function(1.0, 0.0)))
        # fade in background
        self.in_minutes_seconds(start_minute, start_second + 4.5, start_minute, start_second + 4.5 + 0.25)
        get_effects().add_effect(BrightnessEffect(linear_function(0.0, 1.0)))

        # first noise
        self.in_minutes_seconds(start_minute, start_second + 0.13, start_minute, start_second + 1.17)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 4.0)))
        get_effects().add_effect(Saturation(sin_start_max(0.75, 1.0)))

        # second noise
        self.in_minutes_seconds(start_minute, start_second + 1.41, start_minute, start_second + 2.36)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 4.0)))
        get_effects().add_effect(Saturation(sin_start_max(0.75, 1.0)))

        # third noise
        self.in_minutes_seconds(start_minute, start_second + 3.15, start_minute, start_second + 4.22)
        get_effects().add_effect(BrightnessEffect(sin_start_min(1.0, 4.0)))
        get_effects().add_effect(HueShift(sin_start_min(0, 0.1)))
