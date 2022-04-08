import config
from seqcreator.animations.song import Song
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.rendering.functions.functions_store import const_function


class Under(Song):
    def __init__(self):
        super().__init__("under", 2.45*60*1000, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        # self.elements.set([("whisper", "1"), ("whisper", "3")])
        self.elements.set(self.elements.all())
   
        beats = 8
        hue = 0.0
        for x in range(2, 50, beats):
            timing.beats(x, x+beats)    
            hue += 0.1
            coloring.uniform(color.Color(hue))
            
        
        # beats = 1
        # for x in range(52, 80, beats):
        #     timing.beats(x, x+beats)    
        #     hue += 0.3
        #     coloring.uniform(color.Color(hue))

        timing.beats(52, 80) 
        coloring.uniform(color.LIGHT_PURPLE)
        timing.cycle(1)   
        # masking.brightness_saw(0.6)
        masking.hue_shift(0.6)

        beats = 8
        for x in range(80, 112, beats):
            timing.beats(x, x+beats)    
            hue += 0.3
            coloring.uniform(color.Color(hue))
        
        timing.beats(80, 112) 
        timing.cycle(1)
        masking.saturation_shift(0.6)

        beats = 25
        for x in range(11200, 11600, beats):
            timing.beats(x/100, (x+beats)/100)    
            hue += 0.1
            coloring.uniform(color.Color(hue))

        timing.beats(112, 116) 
        timing.cycle(0.25)   
        masking.brightness_saw(0.6)
        
        beats = 4
        for x in range(116, 180, beats):
            timing.beats(x, x+beats)    
            hue += 0.2
            coloring.uniform(color.Color(hue))

        timing.beats(116, 180) 
        timing.cycle(4)
        masking.brightness_saw(0.8)
        
        # timing.beats(0, 130)    
        # masking.brightness(0.8)
