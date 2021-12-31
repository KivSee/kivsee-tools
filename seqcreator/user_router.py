import logging
from seqcreator.network import manager
from seqcreator.users.sapir.me import Sapir
# from seqcreator.users.amir.me import Amir
# from seqcreator.users.bigler.me import Bigler


class UserRouter(object):

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
            logging.error(e)
            raise Exception(e)

    def route(self, args):
        if args.trigger == "stop":
            manager.stop()
        else:
            try:
                logging.info(f"Trying to play {args.trigger}....")
                self.user.play(args.trigger)
            except Exception as e:
                logging.error(e)
                print(f"Failure for trigger {args.trigger}, error {e} ")
