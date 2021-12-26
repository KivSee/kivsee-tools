# import requests
# from config import *
from animations import baz
from animations import songs
from animations import etta
import argparse

parser = argparse.ArgumentParser(description='Runs animations on objects.')
parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
args = parser.parse_args()
print(args.trigger)

###################################
#               BAZ               #
###################################
if args.trigger == "baz":
    trigger_name = "baz"
    baz.register_sequence()
    baz.play_animation()

###################################
#               ETTA              #
###################################
elif args.trigger == "etta":
    trigger_name = "etta"
    etta.register_sequence()
    songs.play("etta")

elif args.trigger == "stop":
    songs.stop()
