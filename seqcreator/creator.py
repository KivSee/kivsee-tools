import argparse
from seqcreator import config
from seqcreator.logging import kivsee_logger
from seqcreator.logging.kivsee_logger import kivseeLogger as logger
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
    kivsee_logger.init()
    logger.info(f"\n---------\nInput argument:\n\ttrigger: {args.trigger}\n---------\n")

    # ---------------------------------
    #        Route user request       #
    # ---------------------------------
    user_router = UserRouter(config.name)
    user_router.route(args.trigger)

