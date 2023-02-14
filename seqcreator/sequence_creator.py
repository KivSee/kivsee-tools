from seqcreator.infra.logger import kivsee_logger as logger
from seqcreator.infra import network_manager
from seqcreator.users.amir.amir import Amir
from seqcreator.users.sapir.sapir import Sapir
from seqcreator.users.bigler.bigler import Bigler
from seqcreator.users.peacock.peacock import Peacock

def run(user, trigger,  offset: int):
    
    # -------------------------------------
    #       User specfic triggering       #
    # -------------------------------------
    if user == "amir":
        user = Amir()
        pass
    elif user == "bigler":
        user = Bigler()
        pass
    elif user == "sapir":
        user = Sapir()
        pass
    elif user == "peacock":
        user = Peacock()
        pass
    else:
        e = f"User {user} does not exists. Make sure it was defined in a .env file."
        raise Exception(e)

    if trigger == "stop":
        network_manager.stop()
    else:
        try:
            logger.info(f"Building and playing {trigger} with offset {offset}....")
            user.play(trigger, offset)
        except Exception as e:
            logger.error(f"Failure for trigger {trigger}, error msg: {e} ")
            raise e
