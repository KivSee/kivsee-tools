from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.brightness import Brightness
from seqcreator.rendering.effects.saturation import Saturation
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import linear_function, sin_function


# Hue modifications:

def hue_shift(offset_factor):
    get_effects().add_effect(HueShift(linear_function(0, offset_factor)))

# Brightness modifications:


def brightness(mult_factor):
    get_effects().add_effect(Brightness(sin_function(0, mult_factor)))


def fade_out():
    get_effects().add_effect(Brightness(linear_function(1, 0)))

# Saturation modifications:


def saturation(mult_factor):
    get_effects().add_effect(Saturation(linear_function(0, mult_factor)))
