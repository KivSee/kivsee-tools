import argparse


import logging
from seqcreator.logging.logger import kivsee_logger as logger
from seqcreator.network import manager
from seqcreator.users.sapir.sapir import Sapir
# from seqcreator.users.amir.amir import Amir
# from seqcreator.users.bigler.bigler import Bigler


def run(user, trigger):
    
    # -------------------------------------
    #       User specfic triggering       #
    # -------------------------------------
    if user == "amir":
        # user = Amir()
        pass
    elif user == "bigler":
        # user = Bigler()
        pass
    elif user == "sapir":
        user = Sapir()
        pass
    else:
        e = f"User {user} does not exists. Make sure it was defined in a .env file."
        raise Exception(e)

    if trigger == "stop":
        manager.stop()
    else:
        try:
            logger.info(f"Building and playing {trigger}....")
            user.play(trigger)
        except Exception as e:
            logger.error(f"Failure for trigger {trigger}, error msg: {e} ")
            raise e
