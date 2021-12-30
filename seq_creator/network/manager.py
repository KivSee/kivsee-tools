import requests
import config


def stop():
    print(f"Triggering stop")
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/stop")
    print(response)
    return response


def play_song(trigger_name):
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/song/{trigger_name}/play")
    print(f"Triggering song {trigger_name} | status code {response.status_code}")
    return response


def play_animation(trigger_name):
    response = requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{trigger_name}")
    print(f"Triggering animation {trigger_name} | status code {response.status_code}")
    return response


def store_sequence_thing(trigger_name, seq, thing_name):
    response = requests.put(
        f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
        json=seq)
    print(f"Storing sequence: {trigger_name} | {thing_name} | status code {response.status_code}")
    if (response.status_code != 200):
        print(response.content)

def store_sequence_all(trigger_name, seq,  thing_names):
    for thing_name in thing_names:
        print(f"Storing for thing {thing_name}")
        store_sequence_thing(trigger_name, seq, thing_name)


def get_segments(thing_name):
    print(f"Getting segments of {thing_name}")
    return requests.get(f"{config.raspberry_pi_addr}:{config.object_service_port}/led-object/{thing_name}")

