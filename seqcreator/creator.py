import argparse
import logging
import sys
from seqcreator import config
from seqcreator.user_router import UserRouter


def run():
    # ---------------------------------
    #         Argument Parser         #
    # ---------------------------------
    parser = argparse.ArgumentParser(description='Runs animations on objects.')
    parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
    # parser.add_argument('-u', dest='user', type=str, help='oneof {amir, bigler, sapir}')
    args = parser.parse_args()

    # ---------------------------------
    #           Logger setup          #
    # ---------------------------------
    # logging.propagate = False
    log = logging.getLogger('')
    log.setLevel(config.log_level)
    formatter = logging.Formatter(fmt="%(asctime)s.%(msecs)03d | %(name)s | %(levelname)s | %(filename)s:%(funcName)s() | line %(lineno)s | %(message)s",
                                  datefmt='%d-%m-%Y %H:%M:%S')
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    logging.StreamHandler().setFormatter(formatter)
    # logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info(f"\n---------\nInput argument:\n\ttrigger: {args.trigger}\n---------\n")

    # ---------------------------------
    #        Route user request       #
    # ---------------------------------
    user_router = UserRouter(config.name)
    user_router.route(args)


run()
