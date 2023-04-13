
import random
from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.api.color import Color
from seqcreator.rendering.effects.rainbow import Rainbow

from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function
from seqcreator.segment_utils import as_symmetric

all_elements_single = [("peacock1", "wing_l"), ("peacock1", "wing_r"), ("peacock1", "body"), ("peacock1", "tail"), ("peacock1", "head")]
all_elements = [("peacock1", "all")]

def uniform(elements, options):
    #elements.set(all_elements)
    hue = getattr(options, 'hue', random.random())
    get_effects().add_effect(ConstColor(Color(hue, 1.0, 1.0)))
    return hue

def gradient(elements, options):
    #elements.set(as_symmetric(all_elements_single))
    hue = options.get('hue', random.random())
    intensity = options.get('intensity', 0.25)
    hue_shift = intensity * 0.15 / 0.25
    get_effects().add_effect(Rainbow(const_function(hue), const_function(hue + hue_shift)))

def rainbow(elements, options):
    #elements.set(as_symmetric(all_elements_single))
    hue = options.get('hue', random.random())
    intensity = options.get('intensity', 0.5)
    hue_shift = intensity * 8
    get_effects().add_effect(Rainbow(const_function(hue), const_function(hue + hue_shift)))

def get_random_coloring(elements, options):
    col = random.choice([uniform])
    # col = random.choice([uniform, gradient, rainbow])
    col(elements, options)