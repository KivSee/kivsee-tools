import random
from seqcreator.api import masking


from seqcreator.api import timing
from seqcreator.api.context import get_energy, use_energy
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.snake import SnakeEffect
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, half_function, linear_function, sin_function, steps_function
from seqcreator.rendering.effects.brightness import Brightness as BrightnessEffect 

all_elements_single = [("peacock1", "wing_l"), ("peacock1", "wing_r"), ("peacock1", "body"), ("peacock1", "tail"), ("peacock1", "head")]
all_elements_single_sym = [("peacock1", "wing_l_s"), ("peacock1", "wing_r_s"), ("peacock1", "body_s"), ("peacock1", "tail_s"), ("peacock1", "head_s")]
all_elements = [("peacock1", "all")]
all_elements_a1 = [("peacock1", "all_a1")]
all_elements_a2 = [("peacock1", "all_a2")]
group_1 = [("peacock1", "wing_l"), ("peacock1", "wing_r")]
group_2 = [("peacock1", "body"), ("peacock1", "tail"), ("peacock1", "head")]

def brightness_sin(elements, options):
    timing.cycle(1)
    elements.set(all_elements)
    masking.brightness_sin(0.3, 1)

def brightness_saw_rising(elements, options):
    timing.cycle(2)
    elements.set(all_elements)
    masking.brightness_saw(0.3, 1)

def brightness_saw_falling(elements, options):
    timing.cycle(2)
    elements.set(all_elements)
    masking.brightness_saw(1.0, 0.3)

def sin_group(elements, options):
    timing.cycle(2)
    elements.set(group_1)
    get_effects().add_effect(BrightnessEffect(sin_function(
        0.2, 1.0, 0.5, 1)))

    elements.set(group_2)
    get_effects().add_effect(BrightnessEffect(sin_function(
        0.2, 1.0, 0, 1)))
    
def blink_group(elements, options):
    timing.cycle(2)
    elements.set(group_1)
    get_effects().add_effect(BrightnessEffect(half_function(const_function(0.2), const_function(1.0))))
    elements.set(group_2)
    get_effects().add_effect(BrightnessEffect(half_function(const_function(1.0), const_function(0.2))))

def brightness_step(elements, options):
    elements.set(all_elements)
    timing.cycle(4)
    get_effects().add_effect(BrightnessEffect(steps_function(8, 0.125, 0.125)))

def alternate_blink(elements, options):
    timing.cycle(2)
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(half_function(const_function(0.2), const_function(1.0))))
    elements.set(all_elements_a2)
    get_effects().add_effect(BrightnessEffect(half_function(const_function(1.0), const_function(0.2))))

def alternate_sin(elements, options):
    timing.cycle(1)
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(sin_function(0.1, 1.0, 0, 1)))
    elements.set(all_elements_a2)
    get_effects().add_effect(BrightnessEffect(sin_function(0.1, 1.0, 0.25, 1)))

def hue_shift_sin(elements, options):
    timing.cycle(2)
    elements.set(all_elements)
    get_effects().add_effect(HueShift(sin_function(-0.1, 0.1, 0, 1)))

def hue_shift_saw_rising(elements, options):
    timing.cycle(2)
    elements.set(all_elements)
    get_effects().add_effect(HueShift(linear_function(0.0, 0.2)))

def hue_shift_group(elements, options):
    timing.cycle(2)
    elements.set(group_1)
    get_effects().add_effect(HueShift(half_function(const_function(0.0), const_function(0.2))))
    elements.set(group_2)
    get_effects().add_effect(HueShift(half_function(const_function(0.2), const_function(0.0))))

def snake(elements, options):
    energy = get_energy()
    density = options.get("density", random.random())
    int_energy = int(energy * 4)
    snake_length = density * 1.9 + 0.1
    timing.cycle(2 ** (4 - int_energy) * 0.25)
    elements.set([("peacock1", "wing_l"), ("peacock1", "wing_r"), ("peacock1", "tail")])
    get_effects().add_effect(SnakeEffect(linear_function(0.0, 1.0), const_function(snake_length), True))

def moving_shadow(elements, options):
    options = options.copy()
    options["density"] = 1.0
    with use_energy(0.5):
        snake(elements, options)

def party_snake(elements, options):
    options = options.copy()
    options["density"] = 0.01
    with use_energy(0.5):
        snake(elements, options)

def confetti(elements, options):
    energy = get_energy()
    density = options.get("density", random.random())
    snake_length = density * 0.8 + 0.2
    timing.cycle((1.0 - energy) * 3.5 + 0.5)
    elements.set([("peacock1", "wing_l_r"), ("peacock1", "wing_r_r"), ("peacock1", "tail_r")])
    get_effects().add_effect(SnakeEffect(linear_function(0.0, 1.0), const_function(snake_length), True))

def conffetti_party(elements, options):
    options = options.copy()
    options["density"] = 0.75
    with use_energy(0.85):
        confetti(elements, options)

def conffetti_chill(elements, options):
    options = options.copy()
    options["density"] = 1.0
    with use_energy(0.01):
        confetti(elements, options)

def snake_grow_shrink(elements, options):
    timing.cycle(4)
    elements.set(all_elements_single_sym)
    get_effects().add_effect(SnakeEffect(sin_function(0.5, 1.0, 0.0, 1.0), sin_function(0.2, 2.0, 0.0, 1.0), True))

def snake_step(elements, options):
    timing.cycle(4)
    elements.set(all_elements_single_sym)
    get_effects().add_effect(SnakeEffect(steps_function(8, 0.125, 0.125), const_function(1.0), True))


def get_random_masking(elements, options):
    # col = random.choice([party_snake])
    col = random.choice([confetti, snake_step, snake_grow_shrink, snake, hue_shift_saw_rising, hue_shift_sin, alternate_sin, alternate_blink, brightness_step, blink_group, sin_group, brightness_saw_falling, brightness_saw_rising, brightness_sin])
    col(elements, options)