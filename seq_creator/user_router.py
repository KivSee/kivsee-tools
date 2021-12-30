import config
from network import manager
from users.sapir.me import Sapir
# from users.amir.me import Amir
# from users.bigle.me import Bigler


class UserRouter(object):

    def __init__(self):
        if (config.name == "amir"):
            # self.user = Amir()
            pass
        elif (config.name == "bigler"):
            # self.user = Bigler()
            pass
        elif (config.name == "sapir"):
            self.user = Sapir()
            pass
        else:
            raise Exception(f"User {config.name} does not exists. Check config file.")


    def route(self, args):
        if args.trigger == "stop":
            manager.stop()
        else:
            try:
                print(f"Trying to play {args.trigger}....")
                self.user.play(args.trigger)
            except Exception as e:
                print(f"Failure for trigger {args.trigger}, error {e} ")


