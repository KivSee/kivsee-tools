from abc import abstractmethod
from typing import Tuple
import typing
from seqcreator.animations.animation import Animation
from seqcreator.api.timing import TimeFrame, set_timing
import seqcreator.api.context.timing as timing
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger

class Song(Animation):

    def __init__(self, trigger, duration, repeats):
        super(Song, self).__init__(trigger, duration, repeats)

    def load(self):
        logger.info(f"loading trigger config {self.trigger_name}")
        self.trigger_config = network_manager.get_trigger_config(self.trigger_name)

    def play(self, offset: int):
        logger.info(f"load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"playing {self.trigger_name}")
        network_manager.play_song(self.trigger_name, offset*1000)

    def in_beats(self, start_beat, end_beat):
        start_section, start_beat_in_section = self._find_beat_section(start_beat)
        end_section, end_beat_in_section = self._find_beat_section(end_beat - 1)
        same_section = start_section == end_section
        num_beats = end_beat - start_beat if same_section else None

        start_ms = Song._beat_start_time(start_section, start_beat_in_section)
        end_ms = Song._beat_end_time(end_section, end_beat_in_section)

        timing.set_timing(timing.KivseeTimeFrame(start_ms, end_ms, num_beats))

    def in_episodes(self, start_episode, end_episode):

        # find the sections for each episode
        start_section, start_episode_section_index = self._find_episode_section(start_episode)
        end_section, end_episode_section_index = self._find_episode_section(end_episode - 1)
        same_section = start_section == end_section
        num_beats = (end_episode - start_episode) * start_section["beatsPerEpisode"] if same_section else None

        start_ms = Song._episode_start_time(start_section, start_episode_section_index)
        end_ms = Song._episode_end_time(end_section, end_episode_section_index)

        timing.set_timing(timing.KivseeTimeFrame(start_ms, end_ms, num_beats))

    def in_episode(self, episode_index):
        self.in_episodes(episode_index, episode_index + 1)

    def with_cycle(self, beats_per_cycle: float, start_beat: typing.Optional[float] = None, end_beat: typing.Optional[float] = None):
        start_beat = start_beat or 0
        end_beat = end_beat or beats_per_cycle
        if start_beat < 0 or start_beat >= end_beat or end_beat > beats_per_cycle:
            raise Exception("Invalid cycle range, must be 0 <= start_beat < end_beat <= beats_per_cycle")
        start_rel_in_cycle = start_beat / beats_per_cycle
        end_rel_in_cycle = end_beat / beats_per_cycle
        timing.set_cycle(timing.KivseeTimeFrameCycle(beats_per_cycle, start_rel_in_cycle, end_rel_in_cycle))

    def _episode_end_time(section, episode_index_in_section: float):
        return Song._episode_start_time(section, episode_index_in_section + 1)

    def _episode_start_time(section, episode_index_in_section: float):

        section_start_time_ms = section["startSeconds"] * 1000
        section_bpm = section["bpm"]
        section_beats_per_episode = section["beatsPerEpisode"]

        episode_start_beat_in_section = episode_index_in_section * section_beats_per_episode
        episode_start_time_ms_in_section = (60.0 * 1000.0 * episode_start_beat_in_section) / section_bpm

        episode_start_time_ms = section_start_time_ms + episode_start_time_ms_in_section

        return episode_start_time_ms
    
    def _beat_end_time(section, beat_index_in_section: float):
        return Song._beat_start_time(section, beat_index_in_section + 1)

    def _beat_start_time(section, beat_index_in_section: float):
        section_start_time_ms = section["startSeconds"] * 1000
        section_bpm = section["bpm"]

        beat_start_time_ms_in_section = (60.0 * 1000.0 * beat_index_in_section) / section_bpm
        beat_start_time_ms = section_start_time_ms + beat_start_time_ms_in_section
        return beat_start_time_ms        

    def _find_beat_section(self, beat_global_index: float) -> Tuple[any, int]:
        current_section_first_beat = 0
        for section in self.trigger_config["bpmSections"]:

            num_episodes = section["numEpisodes"]
            section_beats_per_episode = section["beatsPerEpisode"]
            num_beats = num_episodes * section_beats_per_episode

            next_section_first_beat = current_section_first_beat + num_beats
            if beat_global_index <= next_section_first_beat:
                beat_index_in_section = beat_global_index - current_section_first_beat
                return section, beat_index_in_section
            current_section_first_beat = next_section_first_beat
        return None, None

    def _find_episode_section(self, episode_global_index: float) -> Tuple[any, int]:
        current_section_first_episode = 0
        for section in self.trigger_config["bpmSections"]:
            num_episodes = section["numEpisodes"]
            next_section_first_episode = current_section_first_episode + num_episodes
            if episode_global_index < next_section_first_episode:
                episode_index_in_section = episode_global_index - current_section_first_episode
                return section, episode_index_in_section
            current_section_first_episode = next_section_first_episode
        return None, None