
from seqcreator.infra.color import Color
from seqcreator.rendering.effects import const_color
from seqcreator.rendering.effects_factory import get_effects


def uniform(color: Color):
    get_effects().add_effect(const_color.ConstColor(color))
