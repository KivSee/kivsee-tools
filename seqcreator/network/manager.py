import requests
import config
from seqcreator.logging.logger import kivsee_logger as logger


def stop():
    logger.debug("Triggering stop")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/stop")
    logger.info(f"Stop response {response.status_code}")
    return response


def play_song(trigger_name):
    logger.debug("Playing song")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/song/{trigger_name}/play")
    logger.info(f"Triggering song {trigger_name} - status code ({response.status_code})")
    return response


def play_animation(trigger_name):
    logger.debug("Playing animation")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{trigger_name}")
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


def store_sequence_all(trigger_name, seq, thing_names):
    logger.debug(f"Storing sequence of multiple things, amount {len(thing_names)}")
    for thing_name in thing_names:
        logger.debug(f"Storing for thing {thing_name}")
        store_sequence_thing(trigger_name, seq, thing_name)


def get_segments(thing_name):
    logger.debug("Getting segments from service for thing: {thing_name}")
    logger.info(f"Getting segments of {thing_name}")
    return requests.get(f"{config.raspberry_pi_addr}:{config.object_service_port}/led-object/{thing_name}")
