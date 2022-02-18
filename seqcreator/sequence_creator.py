import argparse
import config

import logging
from seqcreator.logging.logger import kivsee_logger as logger
from seqcreator.network import manager
from seqcreator.users.sapir.sapir import Sapir
# from seqcreator.users.amir.amir import Amir
# from seqcreator.users.bigler.bigler import Bigler


def run():
    # ---------------------------------
    #         Argument Parser         #
    # ---------------------------------
    parser = argparse.ArgumentParser(description='Runs animations on objects.')
    parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
    # parser.add_argument('-u', dest='user', type=str, help='oneof {amir, bigler, sapir}')
    args = parser.parse_args()
    logger.warning(f"Input argument: trigger - {args.trigger}")

    # -------------------------------------
    #       User specfic triggering       #
    # -------------------------------------
    if config.user_name == "amir":
        # user = Amir()
        pass
    elif config.user_name == "bigler":
        # user = Bigler()
        pass
    elif config.user_name == "sapir":
        user = Sapir()
        pass
    else:
        e = f"User {config.user_name} does not exists. Make sure it was defined in a .env file."
        raise Exception(e)

    if args.trigger == "stop":
        manager.stop()
    else:
        try:
            logger.info(f"Building and playing {args.trigger}....")
            user.play(args.trigger)
        except Exception as e:
            logger.error(f"Failure for trigger {args.trigger}, error msg: {e} ")
            raise e
