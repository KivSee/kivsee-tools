# import requests
# from config import *
from users.sapir.songs import etta, baz, under2, under_basic
from users.sapir.songs.under import Under
from network import manager
import argparse

# ---------------------------------
#               Parser            #
# ---------------------------------
parser = argparse.ArgumentParser(description='Runs animations on objects.')
parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
# TODO sapir add log levels filtering
parser.add_argument('-v', dest='logging', type=str, help='log level to print')
parser.add_argument('-u', dest='user', type=str, help='oneof {amir, bigler, sapir}')
args = parser.parse_args()
print(f"Input argument:\n\ttrigger: {args.trigger}\n\tlogging: {args.logging}\n\tuser: {args.user}")


if args.trigger == "baz":
    baz.build_and_store_sequence()
    manager.play_animation(args.trigger)

elif args.trigger == "etta":
    etta.build_and_store_sequence()
    manager.play_song(args.trigger)

elif args.trigger == "under_basic":
    under_basic.build_and_store_sequence()
    manager.play_song("under")

elif args.trigger == "under":
    under = Under()
    under.play()

elif args.trigger == "stop":
    manager.stop()