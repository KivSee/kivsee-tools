import argparse
import config

from seqcreator.logging.logger import kivsee_logger as logger
from seqcreator.router import Router

def run():
    # ---------------------------------
    #         Argument Parser         #
    # ---------------------------------
    parser = argparse.ArgumentParser(description='Runs animations on objects.')
    parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
    # parser.add_argument('-u', dest='user', type=str, help='oneof {amir, bigler, sapir}')
    args = parser.parse_args()
    logger.warning(f"Input argument: trigger - {args.trigger}")

    # ---------------------------------
    #        Route user request       #
    # ---------------------------------
    users = Router(config.user_name)
    users.route(args.trigger)

