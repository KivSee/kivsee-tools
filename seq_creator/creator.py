from user_router import UserRouter
import argparse

def run():
# ---------------------------------
    #         Argument Parser         #
    # ---------------------------------
    parser = argparse.ArgumentParser(description='Runs animations on objects.')
    parser.add_argument('-t', dest='trigger', type=str, help='the name of the song or animation to play')
    # TODO sapir add log levels filtering
    parser.add_argument('-v', dest='logging', type=str, help='log level to print')
    # parser.add_argument('-u', dest='user', type=str, help='oneof {amir, bigler, sapir}')
    args = parser.parse_args()
    print(f"Input argument:\n\ttrigger: {args.trigger}\n\tlogging: {args.logging}\n")


    # ---------------------------------
    #        Route user request       #
    # ---------------------------------
    user_router = UserRouter()
    user_router.route(args)

run()

