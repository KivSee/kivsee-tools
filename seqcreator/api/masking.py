from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.brightness import Brightness
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import linear_function


def hue_shift(offset_factor):
    get_effects().add_effect(HueShift(linear_function(0, 1)))


def brightness(mult_factor):
    get_effects().add_effect(Brightness(linear_function(0, 1)))
