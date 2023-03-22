from seqcreator.rendering.effects.hue_shift import HueShift as HueShiftEffect
from seqcreator.rendering.effects.brightness import Brightness as BrightnessEffect 
from seqcreator.rendering.effects.saturation import Saturation as SaturationEffect
from seqcreator.rendering.effects.snake import SnakeEffect
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, linear_function, repeat_function, sin_function

# Snake effect:
def snake():
    get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(1)))

def snake_bidrectional():
    get_effects().add_effect(SnakeEffect(sin_function(0, 1, -0.25, 1), const_function(1)))

def snake_backward():
    get_effects().add_effect(SnakeEffect(linear_function(2, 0), const_function(1)))

# def snake_custom(head: int, tail_length, direction):
#     get_effects().add_effect(SnakeEffect(linear_function(0, 2), const_function(1)))

# Hue modifications:

def hue_shift_const(offset):
    get_effects().add_effect(HueShiftEffect(const_function(offset)))

def hue_shift(offset_factor):
    get_effects().add_effect(HueShiftEffect(linear_function(0, offset_factor)))

# Brightness modifications:

def brightness_sin(min_brightness: int = 0, max_brightness: int = 1, speed: int = 1):
    get_effects().add_effect(BrightnessEffect(sin_function(
        min_brightness, max_brightness, 0, speed)))


def brightness_saw(min_brightness: int = 0, max_brightness: int = 1, repeat: int = 1):
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat, linear_function(
        min_brightness, max_brightness))))


def brightness(mult_factor):
    get_effects().add_effect(BrightnessEffect(const_function(mult_factor)))


def fade_out():
    get_effects().add_effect(BrightnessEffect(linear_function(1, 0)))


def fade_in():
    get_effects().add_effect(BrightnessEffect(linear_function(0, 1)))

# Saturation modifications:


def saturation(mult_factor):
    get_effects().add_effect(SaturationEffect(const_function(mult_factor)))

def saturation_shift(val):
    get_effects().add_effect(SaturationEffect(linear_function(1-val, 1)))
