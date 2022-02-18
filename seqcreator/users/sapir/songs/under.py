from seqcreator.users.sapir.songs.deprecated import under2
from seqcreator.infra import timing
from seqcreator.rendering.function import functions_store
from seqcreator.animations.song import Song


note_to_elem1 = {
    "D": "spiral1",
    "Bb": "spiral2",
    "F": "spiral3",
    "C": "subout1",
    "Eb": "subout2",
    "A": "subout3",
}

note_to_elem2 = {
    "D": "subout4",
    "Bb": "subout5",
    "F": "subout6",
    "C": "subout7",
    "G": "subout8",
    "A": "subout9",
}

notes = ["A", "C", "D", "F", "Bb", "Eb"]

note_to_color = {
    "A": (0.0, 1.0, 1.0),
    "C": (0.15, 1.0, 1.0),
    "D": (0.3, 1.0, 1.0),
    "F": (0.5, 1.0, 1.0),
    "Bb": (0.7, 1.0, 1.0),
    "Eb": (0.85, 1.0, 1.0),
}


class Under(Song):
    def __init__(self, element_provider):
        super().__init__("under", 147000, 0, element_provider)

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)
        timing.beats(2, 20)

        for note in notes:
            # TODO fix with amir - elements provider
            groups_of_segments = [note_to_elem1[note]]
            c = note_to_color[note]
            self.coloring_effect.uniform([c[0], 0.5, 0.3], groups_of_segments)

        start_beat = 2
        end_beat = 10
        timing.beats(start_beat, end_beat)


        self.play_note(start_beat, "D", 0.0)
        self.play_note(start_beat, "F", 0.25)
        self.play_note(start_beat, "Bb", 0.5)
        self.play_note(start_beat, "Bb", 0.75)
        self.play_note(start_beat, "D", 0.75)
        self.play_note(start_beat, "Bb", 1.25)
        self.play_note(start_beat, "D", 1.25)
        self.play_note(start_beat, "F", 1.75)

        self.play_note(start_beat, "A", 2.0)
        self.play_note(start_beat, "C", 2.0)
        self.play_note(start_beat, "C", 2.5)
        self.play_note(start_beat, "Eb", 2.5)
        self.play_note(start_beat, "Bb", 3.0)
        self.play_note(start_beat, "D", 3.0)
        self.play_note(start_beat, "F", 3.5)
        self.play_note(start_beat, "Bb", 3.5)

        self.play_note(start_beat, "Bb", 4.0)
        self.play_note(start_beat, "D", 4.25)
        self.play_note(start_beat, "F", 4.5)
        self.play_note(start_beat, "F", 4.75)
        self.play_note(start_beat, "Bb", 4.75)
        self.play_note(start_beat, "F", 5.25)
        self.play_note(start_beat, "Bb", 5.25)
        self.play_note(start_beat, "C", 5.75)

        self.play_note(start_beat, "F", 6.0)
        self.play_note(start_beat, "A", 6.0)
        self.play_note(start_beat, "Eb", 6.5)
        self.play_note(start_beat, "C", 6.5)
        self.play_note(start_beat, "Bb", 7.0)
        self.play_note(start_beat, "D", 7.0)

        start_beat = 10
        end_beat = 18
        timing.beats(start_beat, end_beat)

        self.play_note(start_beat, "D", 0.0)
        self.play_note(start_beat, "F", 0.25)
        self.play_note(start_beat, "Bb", 0.5)
        self.play_note(start_beat, "Bb", 0.75)
        self.play_note(start_beat, "D", 0.75)
        self.play_note(start_beat, "Bb", 1.25)
        self.play_note(start_beat, "D", 1.25)
        self.play_note(start_beat, "F", 1.75)

        self.play_note(start_beat, "A", 2.0)
        self.play_note(start_beat, "C", 2.0)
        self.play_note(start_beat, "C", 2.5)
        self.play_note(start_beat, "Eb", 2.5)
        self.play_note(start_beat, "Bb", 3.0)
        self.play_note(start_beat, "D", 3.0)
        self.play_note(start_beat, "F", 3.5)
        self.play_note(start_beat, "Bb", 3.5)

        self.play_note(start_beat, "Bb", 4.0)
        self.play_note(start_beat, "D", 4.25)
        self.play_note(start_beat, "F", 4.5)
        self.play_note(start_beat, "F", 4.75)
        self.play_note(start_beat, "Bb", 4.75)
        self.play_note(start_beat, "F", 5.25)
        self.play_note(start_beat, "Bb", 5.25)
        self.play_note(start_beat, "C", 5.75)

        self.play_note(start_beat, "F", 6.0)
        self.play_note(start_beat, "A", 6.0)
        self.play_note(start_beat, "Eb", 6.5)
        self.play_note(start_beat, "C", 6.5)
        self.play_note(start_beat, "Bb", 7.0)
        self.play_note(start_beat, "D", 7.0)


    def play_note(self, start_beat, note, t):
        start = start_beat + t
        end = start_beat + t + 0.5
        timing.beats(start, end)
        groups_of_segments = [note_to_elem1[note]]
        factor = 1.5
        function_decrease = functions_store.linear_function(factor * 1.0, factor * 0.5)
        self.masking_effect.brightness(function_decrease, groups_of_segments)
