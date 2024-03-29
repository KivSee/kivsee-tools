
import random
from seqcreator.api.context.energy import get_energy
from seqcreator.api.context.hue import get_hues, get_primary_hue
from seqcreator.rendering.effects.const_color import ConstColor
from seqcreator.api.color import Color
from seqcreator.rendering.effects.rainbow import Rainbow

from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function
from seqcreator.segment_utils import as_symmetric

all_elements_single = [("peacock1", "wing_l"), ("peacock1", "wing_r"), ("peacock1", "body"), ("peacock1", "tail"), ("peacock1", "head")]
all_elements = [("peacock1", "all")]

def uniform(elements):
    elements.set(all_elements)
    hue = get_primary_hue()
    brightness = get_energy(0.5) * 0.9 + 0.1
    get_effects().add_effect(ConstColor(Color(hue, 1.0, brightness)))

def gradient(elements):
    elements.set(as_symmetric(all_elements_single))
    primary_hue, secondary_hue = get_hues(0.0)
    if secondary_hue is None:
        # hue shift based on the energy.
        # not too much though, we want it gradient and not rainbow
        energy = get_energy(0.5)
        hue_shift = energy / 3 # max hue shift is 0.33 for full energy
        orig_primary_hue = primary_hue
        primary_hue = orig_primary_hue - hue_shift / 2
        secondary_hue = orig_primary_hue + hue_shift / 2
    get_effects().add_effect(Rainbow(const_function(primary_hue), const_function(secondary_hue)))

def rainbow(elements):
    elements.set(as_symmetric(all_elements_single))
    primary_hue = get_primary_hue(0.0)
    energy = get_energy(0.5)
    hue_shift = int(energy * 4)
    get_effects().add_effect(Rainbow(const_function(primary_hue), const_function(primary_hue + hue_shift)))

def get_random_coloring(elements):
    energy = get_energy(0.5)
    uniform_wieght = 1.0 - abs(0.0 - energy)
    gradient_wieght = 1.0 - abs(0.5 - energy)
    rainbow_wieght = 1.0 - abs(1.0 - energy)
    col = random.choices([uniform, gradient, rainbow], [uniform_wieght, gradient_wieght, rainbow_wieght])[0]
    col(elements)