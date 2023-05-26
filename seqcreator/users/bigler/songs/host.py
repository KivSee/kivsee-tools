from seqcreator.api.color import Color
from seqcreator.api import coloring
from seqcreator.api import timing
from seqcreator.api import masking
from seqcreator.api import element_provider
from seqcreator.rendering.functions import functions_store
from seqcreator.animations.song import Song



class Host(Song):
    def __init__(self):
        super().__init__("host", 473000, 1)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=123, beats_per_episode=32, start_offset=0)
        beats = 957
        timing.beats(0, beats)

        # for note in notes:
            # TODO fix with amir - elements provider
            # groups_of_segments = [note_to_elem1[note]]
            # c = note_to_color[note]
            # element_provider.set_current([])
            # coloring.uniform(color.blue)

        self.elements.set(self.elements.all())
        # coloring.uniform(Color(0.0, 1.0, 0.5))

        start_beat = 0
        # end_beat = 10
        # timing.beats(start_beat, end_beat)
        coloring.uniform(Color(0.1, 1.0, 0.5))

        for beat in range(start_beat,beats,4):
            self.play_beat(beat, 0.0)
            # self.play_beat(beat, elements[1], 1.0)
            # self.play_beat(beat, elements[2], 2.0)


    def play_beat(self, start_beat, t):
        start = start_beat + t
        end = start_beat + t + 0.5
        timing.beats(start, end)
        # factor = 1.5
        # function_decrease = functions_store.linear_function(factor * 1.0, factor * 0.5)
        # masking.fade_out()
        masking.brightness_saw(0,1,4)
