import requests
import config
from seqcreator.infra.logger import kivsee_logger as logger


def stop():
    logger.debug("Triggering stop")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/stop")
    logger.info(f"Stop response {response.status_code}")
    return response


def play_song(trigger_name, start_offset_ms:int = 0):
    logger.debug("Playing song")
    trigger_song_options ={"start_offset_ms": start_offset_ms}
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/song/{trigger_name}/play", json=trigger_song_options)
    logger.info(f"Triggering song {trigger_name} - status code ({response.status_code})")
    return response


def play_soundless_animation(trigger_name, start_offset_ms:int = 0):
    logger.debug("Playing animation")
    trigger_animation_options = {"start_offset_ms": start_offset_ms}
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{trigger_name}", json=trigger_animation_options)
    logger.info(f"Triggering animation {trigger_name} - status code ({response.status_code})")
    return response


def store_sequence_thing(trigger_name, seq, thing_name):
    logger.debug("Storing sequence of a thing")
    response = requests.put(
        f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
        json=seq)
    logger.info(
        f"Storing sequence: {trigger_name} for {thing_name} - status code ({response.status_code})")
    if response.status_code != 200:
        logger.error(f"{response.content}")


def store_sequence_all(trigger_name, per_thing_config):
    logger.debug(f"Storing sequence of multiple things, amount {len(per_thing_config)}")
    response = requests.put(
        f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{trigger_name}",
        json=per_thing_config)
    logger.info(
        f"Storing sequence: {trigger_name} - status code ({response.status_code})")
    if response.status_code != 200:
        logger.error(f"{response.content}")

def get_segments(thing_name):
    logger.debug("Getting segments from service for thing: {thing_name}")
    logger.info(f"Getting segments of {thing_name}")
    return requests.get(f"{config.raspberry_pi_addr}:{config.object_service_port}/thing/{thing_name}")


def get_all_segments():
    logger.info(f"Getting all segments of all things")
    response = requests.get(f"{config.raspberry_pi_addr}:{config.object_service_port}/thing")
    logger.info(
        f"Get all segments - status code ({response.status_code})")
    return response.content