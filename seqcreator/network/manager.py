import requests
import logging
from seqcreator import config

logger = logging.getLogger(__name__)

def stop():
    logger.debug("Network.Manager::Triggering stop")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/stop")
    logger.info(f"Network.Manager::stop response {response.status_code}")
    return response


def play_song(trigger_name):
    logger.debug("Network.Manager::Playing song")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/song/{trigger_name}/play")
    logger.info(f"Network.Manager::Triggering song {trigger_name} | status code {response.status_code}")
    return response


def play_animation(trigger_name):
    logger.debug("Network.Manager::Playing animation")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{trigger_name}")
    logger.info(f"Network.Manager::Triggering animation {trigger_name} | status code {response.status_code}")
    return response


def store_sequence_thing(trigger_name, seq, thing_name):
    logger.debug("Network.Manager::Storing sequence of a thing")
    response = requests.put(
        f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
        json=seq)
    logger.info(
        f"Network.Manager::Storing sequence: {trigger_name} | {thing_name} | status code {response.status_code}")
    if response.status_code != 200:
        logger.error(f"Network.Manager::{response.content}")


def store_sequence_all(trigger_name, seq, thing_names):
    logger.debug(f"Network.Manager::Storing sequence of multiple things, amount {len(thing_names)}")
    for thing_name in thing_names:
        logger.debug(f"Network.Manager::Storing for thing {thing_name}")
        store_sequence_thing(trigger_name, seq, thing_name)


def get_segments(thing_name):
    logger.debug("Network.Manager::Getting segments from service for thing: {thing_name}")
    logger.info(f"Network.Manager::Getting segments of {thing_name}")
    return requests.get(f"{config.raspberry_pi_addr}:{config.object_service_port}/led-object/{thing_name}")
