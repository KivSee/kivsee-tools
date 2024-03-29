import random
from seqcreator.api import masking


from seqcreator.api import timing
from seqcreator.rendering.effects.hue_shift import HueShift
from seqcreator.rendering.effects.snake import SnakeEffect
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.rendering.functions.functions_store import const_function, half_function, linear_function, repeat_function, sin_function, steps_from_to, steps_function
from seqcreator.rendering.effects.brightness import Brightness as BrightnessEffect 

all_elements_single = [("peacock1", "wing_l"), ("peacock1", "wing_r"), ("peacock1", "body"), ("peacock1", "tail"), ("peacock1", "head")]
all_elements_single_sym = [("peacock1", "wing_l_s"), ("peacock1", "wing_r_s"), ("peacock1", "body_s"), ("peacock1", "tail_s"), ("peacock1", "head_s")]
all_elements = [("peacock1", "all")]
all_elements_a1 = [("peacock1", "all_a1")]
all_elements_a2 = [("peacock1", "all_a2")]
group_1 = [("peacock1", "wing_l"), ("peacock1", "wing_r")]
group_2 = [("peacock1", "body"), ("peacock1", "tail"), ("peacock1", "head")]

def brightness_sin(elements, options):
    # timing.cycle(16)
    #elements.set(all_elements)
    masking.brightness_sin(0.0, 0.6)

def brightness_saw_rising(elements, options):
    # timing.cycle(8)
    elements.set(all_elements)
    masking.brightness_saw(0.2, 1.0)

def brightness_saw_falling(elements, options):
    # timing.cycle(2)
    elements.set(all_elements)
    masking.brightness_saw(1.0, 0.3)

def sin_group(elements, options):
    # timing.cycle(2)
    elements.set(group_1)
    get_effects().add_effect(BrightnessEffect(sin_function(
        0.2, 1.0, 0.5, 1)))

    elements.set(group_2)
    get_effects().add_effect(BrightnessEffect(sin_function(0.2, 1.0, 0, 1)))
    
def blink_group(elements, options):
    #timing.cycle(2)
    elements.set(group_1)
    get_effects().add_effect(BrightnessEffect(half_function(const_function(0.2), const_function(1.0))))
    elements.set(group_2)
    get_effects().add_effect(BrightnessEffect(half_function(const_function(1.0), const_function(0.2))))

def brightness_step(elements, options):
    elements.set(all_elements)
    timing.cycle(4)
    get_effects().add_effect(BrightnessEffect(steps_function(8, 0.125, 0.125)))

def alternate_blink(elements, repeat_times):
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat_times, half_function(const_function(0.2), const_function(1.0)))))
    elements.set(all_elements_a2)
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat_times, half_function(const_function(1.0), const_function(0.2)))))

def half_alternate_blink(elements, repeat_times):
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat_times, half_function(const_function(0.2), const_function(1.0)))))

def half_alternate_blank(elements):
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(const_function(0.0)))

def alternate_sin(elements, repeat_times):
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat_times, sin_function(0.0, 0.4, 0, 1))))
    elements.set(all_elements_a2)
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat_times, sin_function(0.0, 0.4, 0.25, 1))))

def half_alternate_sin(elements, repeat_times):
    elements.set(all_elements_a1)
    get_effects().add_effect(BrightnessEffect(repeat_function(repeat_times, sin_function(0.0, 0.4, 0, 1))))

def hue_shift_sin(elements, options):
 #   timing.cycle(2)
    elements.set(all_elements)
    get_effects().add_effect(HueShift(sin_function(-0.1, 0.1, 0, 1)))

def hue_shift_saw_rising(elements, options):
  #  timing.cycle(2)
    elements.set(all_elements)
    get_effects().add_effect(HueShift(linear_function(0.0, 0.2)))

def hue_shift_group(elements, options):
   # timing.cycle(2)
    elements.set(group_1)
    get_effects().add_effect(HueShift(half_function(const_function(0.0), const_function(0.2))))
    elements.set(group_2)
    get_effects().add_effect(HueShift(half_function(const_function(0.2), const_function(0.0))))

def snake(elements, options):
    snake_length = random.random() * 5
    #timing.cycle(1)
    elements.set([("peacock1", "wing_l_s"), ("peacock1", "wing_r_s"), ("peacock1", "tail_s")])
    get_effects().add_effect(SnakeEffect(linear_function(0.0, 1.0 + snake_length), const_function(snake_length)))

def snake_grow_shrink(elements, options):
    get_effects().add_effect(SnakeEffect(const_function(0.5), sin_function(0.0, 0.5, 0.0, 1.0), True))

def snake_step(elements, options):
    #timing.cycle(4)
    elements.set(all_elements_single_sym)
    get_effects().add_effect(SnakeEffect(steps_from_to(16, 0, 1), const_function(8.0), False))


def get_random_masking(elements, options):
    # col = random.choice([snake_step])
    col = random.choice([snake_step, snake_grow_shrink, snake, hue_shift_saw_rising, hue_shift_sin, alternate_sin, alternate_blink, brightness_step, blink_group, sin_group, brightness_saw_falling, brightness_saw_rising, brightness_sin])
    col(elements, options)