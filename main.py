import argparse
from objectsetup import configure_segments
from seqcreator import sequence_creator
import config

if __name__ == '__main__':

    # ---------------------------------
    #         Argument Parser         #
    # ---------------------------------
    parser = argparse.ArgumentParser(description='Runs animations on objects.')
    parser.add_argument('-m', dest='mode', type=str, help='the mode: seq or map')
    parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
    args = parser.parse_args()
    
    user = config.user_name

    if args.mode == "seq":
        print(f"This trigger name is {args.trigger}")
        sequence_creator.run(user, str(args.trigger))
    elif args.mode == "map":
        configure_segments.run(user)
