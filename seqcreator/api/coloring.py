
from seqcreator.api.color import Color
from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.rendering.effects.rainbow import Rainbow
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import *


def uniform(color: Color):
    get_effects().add_effect(ConstColor(color))


def rainbow(start: float = 0, end: float = 1, range: int = 1, speed: int = 0):
    get_effects().add_effect(Rainbow(linear_function(start, end + speed),
                                     linear_function(start + range, end + range + speed)))


def rainbow_collide(start: float = 0, end: float = 1):
    get_effects().add_effect(Rainbow(linear_function(
        start, end), linear_function(end, start)))


#TODO: Change to ConstColor from Rainbow (Currently receives identical values for "start" and "end" == constant color)
def hue_range(start: float = 0, end: float = 1, speed: int = 1):
    get_effects().add_effect(Rainbow(sin_function(start, end, 0, speed),
                                     sin_function(start, end, 0, speed)))
