import logging
from seqcreator.network import manager
from seqcreator.users.sapir.me import Sapir
# from seqcreator.users.amir.me import Amir
# from seqcreator.users.bigler.me import Bigler


class Router(object):

    def __init__(self, name):
        if name == "amir":
            # self.user = Amir()
            pass
        elif name == "bigler":
            # self.user = Bigler()
            pass
        elif name == "sapir":
            self.user = Sapir()
            pass
        else:
            e = f"User {name} does not exists. Make sure it was defined in a .env file."
            raise Exception(e)

    def route(self, trigger_name):
        if trigger_name == "stop":
            manager.stop()
        else:
            try:
                # logger.info(f"Building and playing {trigger_name}....")
                self.user.play(trigger_name)
            except Exception as e:
                raise e
                # logger.error(f"Failure for trigger {trigger_name}, error msg: {e} ")
