from seqcreator.infra.objects_provider import ObjectsProvider
from seqcreator.rendering.effects import (rainbow, brightness, hue_shift, const_color)
from seqcreator.rendering.function import functions_store
#  TODO protect it to be package-private
objectsProvider = ObjectsProvider()

class ColoringEffectFactory:

    def __init__(self, segments, effects_list_holder):
        self.effects_list_holder = effects_list_holder
        self.all_segments = segments

    def uniform(self, color, group_of_segments):
        temp_list = const_color.all_segments(group_of_segments, color)
        self.effects_list_holder.extend(temp_list)
        print("uniform done")
        # print(self.effects_list_holder.effects_list)
    #     ConstColorAnimation(color).apply()
    #
    # def gradient(self, hue_start, hue_end):
    #     Rainbow(ConstFloatFunc(hue_start), ConstFloatFunc(hue_end)).apply()
    #
    # def alternate(self, color1, color2, number_of_pixels = 3):
    #     AlternateColoringAnimation(color1, color2, number_of_pixels).apply()

# # TODO to be deleted
# effect333 = []
# coloring_effect = ColoringEffectFactory( "all", effect333 )


class MaskingEffectFactory:

    def __init__(self, segments, effects_list_holder):
        self.effects_list_holder = effects_list_holder
        self.all_segments = segments

    def brightness(self, function, groups_of_segments):
        temp_list = brightness.all_segments(groups_of_segments, function)
        self.effects_list_holder.extend(temp_list)
        print("Done brightness")
    #     BrightnessAnimation(ConstFloatFunc(factor)).apply()
    #
    # def snake(self, tail=1.0, switch_direction=False):
    #     if isinstance(tail, str):
    #         tail = {short: 0.25, medium: 1.0, long: 4.0}[tail]
    #     if switch_direction:
    #         SnakeAnimation(LinearFloatFunc(1.0, 0.0 - tail), ConstFloatFunc(tail), ConstBooleanFunc(not switch_direction)).apply()
    #     else:
    #         SnakeAnimation(LinearFloatFunc(0.0, 1.0 + tail), ConstFloatFunc(tail), ConstBooleanFunc(not switch_direction)).apply()
    #
    # def snake_up_down(self, tail=1.0):
    #     if isinstance(tail, str):
    #         tail = {short: 0.25, medium: 1.0, long: 4.0}[tail]
    #     SnakeAnimation(SinFloatFunc(1.0, -0.1, -0.25, 1), ConstFloatFunc(tail), ConstBooleanFunc(True)).apply()
    #
    # def snake_down_up(self, tail=1.0):
    #     if isinstance(tail, str):
    #         tail = {short: 0.25, medium: 1.0, long: 4.0}[tail]
    #     SnakeAnimation(SinFloatFunc(0.0, 1.0, -0.25, 1), ConstFloatFunc(tail), ConstBooleanFunc(False)).apply()
    #
    # def blink_repeat(self, repeat, edge=0.5):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.25, medium: 0.5, hard: 0.75, total: 1.0}[edge]
    #     BrightnessAnimation(RepeatFloatFunc(repeat, HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - edge)))).apply()
    #
    # def blink(self, edge=0.5, reverse=False):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.25, medium: 0.5, hard: 0.75, total: 1.0}[edge]
    #     v1 = 1.0 - edge if reverse else 1.0
    #     v2 = 1.0 if reverse else 1.0 - edge
    #     BrightnessAnimation(HalfFloatFunc(ConstFloatFunc(v1), ConstFloatFunc(v2))).apply()
    #
    # def breath(self, edge=0.6, reverse=False):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.4, medium: 0.6, hard: 0.8, total: 1.0}[edge]
    #     phase = 0.25 if reverse else -0.25
    #     BrightnessAnimation(SinFloatFunc(1.0 - edge, 1.0, phase, 1)).apply()
    #
    def fade_in(self):
        pass
    #     BrightnessAnimation(LinearFloatFunc(0.0, 1.0)).apply()
    #
    def fade_out(self):
        pass
    #     BrightnessAnimation(LinearFloatFunc(1.0, 0.0)).apply()
    #
    # def saw_tooth(self, edge=0.6, reverse=False):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.4, medium: 0.6, hard: 0.8, total: 1.0}[edge]
    #     min_val = 1.0 - edge if reverse else 1.0
    #     max_val = 1.0 if reverse else 1.0 - edge
    #     BrightnessAnimation(LinearFloatFunc(min_val, max_val)).apply()
    #
    # def hue_shift_steps(self, num_steps, step_jump):
    #     HueShiftAnimation(StepsFloatFunc(num_steps, step_jump, 0.0)).apply()
    #
    # def hue_shift(self, edge=0.5):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.05, medium: 0.12, hard: 0.25, total: 0.5}[edge]
    #     HueShiftAnimation(ConstFloatFunc(edge)).apply()
    #
    # def brightness(self, val):
    #     BrightnessAnimation(ConstFloatFunc(val)).apply()
    #
    # def hue_blink(self, edge=0.5, reverse=False):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.05, medium: 0.12, hard: 0.25, total: 0.5}[edge]
    #     if reverse:
    #         edge = -edge
    #     HueShiftAnimation(HalfFloatFunc(ConstFloatFunc(1.0), ConstFloatFunc(1.0 - edge))).apply()
    #
    # def hue_breath(self, edge=0.1):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.03, medium: 0.1, hard: 0.2, total: 0.5}[edge]
    #     HueShiftAnimation(SinFloatFunc(-edge, edge, 0.0, 1)).apply()
    #
    # def hue_saw_tooth(self, edge=0.1, reverse=False):
    #     if isinstance(edge, str):
    #         edge = {soft: 0.04, medium: 0.08, hard: 0.2, total: 0.35}[edge]
    #     if reverse:
    #         edge = -edge
    #     HueShiftAnimation(LinearFloatFunc(0.0, edge)).apply()
    #
    # def random_brightness(self):
    #     RandBrightnessAnimation().apply()
    #
    # def random_saturation(self):
    #     RandSaturationAnimation().apply()
    #
    # def confetti(self):
    #     ConfettiAnimation(ConstFloatFunc(0.5)).apply()
    #
    # def fill(self):
    #     FillAnimation(ConstFloatFunc(0.0), LinearFloatFunc(0.0, 1.0)).apply()
    #
    # def fill_in_steps(self, num_steps):
    #     FillAnimation(ConstFloatFunc(0.0), StepsFloatFunc(num_steps, 1/num_steps, 1/num_steps)).apply()
    #
    # def fill_out(self, reverse=False):
    #     if reverse:
    #         FillAnimation(LinearFloatFunc(0.0, 1.0), ConstFloatFunc(1.0)).apply()
    #     else:
    #         FillAnimation(ConstFloatFunc(0.0), LinearFloatFunc(1.0, 0.0)).apply()
    #
    # def fill_in_out(self, edge = 1.0):
    #     FillAnimation(ConstFloatFunc(0.0), HalfFloatFunc(LinearFloatFunc(0.0, edge), LinearFloatFunc(edge, 0.0))).apply()
    #
    # def fill_out_in(self, edge = 1.0):
    #     FillAnimation(ConstFloatFunc(0.0), HalfFloatFunc(LinearFloatFunc(1.0, 1-edge), LinearFloatFunc(1-edge, 1.0))).apply()
    #
    # def segment_breath(self, length = 0.25):
    #     FillAnimation(SinFloatFunc(0.0, 1.0 - length, -0.25, 1), SinFloatFunc(length, 1.0, -0.25, 1)).apply()
    #
    # def segment_saw_tooth(self, length = 0.25):
    #     FillAnimation(HalfFloatFunc(LinearFloatFunc(0.0, 1.0 - length), LinearFloatFunc(1.0 - length, 0.0)),
    #                   HalfFloatFunc(LinearFloatFunc(length, 1.0), LinearFloatFunc(1.0, length))).apply()
    #
    # def segment_up(self, length = 0.25):
    #     FillAnimation(LinearFloatFunc(0.0, 1.0 - length),LinearFloatFunc(length, 1.0)).apply()
    #
    # def segment_down(self, length = 0.25):
    #     FillAnimation(LinearFloatFunc(1.0 - length, 0.0),LinearFloatFunc(1.0, length)).apply()
    #
    # def hue_shift_cycle_target(self, start=0.0, end=1.0):
    #     HueShiftCycleAnimation(StepTargetDiscreteFloatFunc(start, end)).apply()
    #
    # def hue_shift_cycle_diff(self, start=0.0, dx=0.25):
    #     HueShiftCycleAnimation(StepDiffDiscreteFloatFunc(start, dx)).apply()

# masking_effect = MaskingEffectFactory()