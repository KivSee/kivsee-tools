from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.brightness import Brightness
from seqcreator.rendering.effects.saturation import Saturation
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, linear_function, repeat_function, sin_function


# Hue modifications:

def hue_shift(offset_factor):
    get_effects().add_effect(HueShift(linear_function(0, offset_factor)))

# Brightness modifications:


def brightness_sin(min_brightness: int = 0, max_brightness: int = 1, speed: int = 1):
    get_effects().add_effect(Brightness(sin_function(
        min_brightness, max_brightness, 0, speed)))


def brightness_saw(min_brightness: int = 0, max_brightness: int = 1, repeat: int = 1):
    get_effects().add_effect(Brightness(repeat_function(repeat, linear_function(
        min_brightness, max_brightness))))


def brightness(mult_factor):
    get_effects().add_effect(Brightness(const_function(mult_factor)))


def fade_out():
    get_effects().add_effect(Brightness(linear_function(1, 0)))


def fade_in():
    get_effects().add_effect(Brightness(linear_function(0, 1)))

# Saturation modifications:


def saturation(mult_factor):
    get_effects().add_effect(Saturation(const_function(mult_factor)))
