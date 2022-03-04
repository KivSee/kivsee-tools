
from seqcreator.api.color import Color
from seqcreator.rendering.effects import const_color, hue_shift
from seqcreator.rendering.effects.rainbow import Rainbow
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import *


def uniform(color: Color):
    get_effects().add_effect(const_color.ConstColor(color))


def rainbow(start: float = 0, end: float = 1, range: int = 1, speed: int = 0):
    get_effects().add_effect(Rainbow(linear_function(start, end + speed),
                                     linear_function(start + range, end + range + speed)))


def rainbow_collide(start: float = 0, end: float = 1):
    get_effects().add_effect(Rainbow(linear_function(
        start, end), linear_function(end, start)))
