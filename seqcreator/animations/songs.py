import requests
import config

def play(trigger_name):
    print(f"Invoke {trigger_name}")
    print(requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/song/{trigger_name}/play"))

def stop():
    print(f"Invoke stop")
    print(requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/stop"))
