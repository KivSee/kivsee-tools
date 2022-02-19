import logging
import sys
import config

logger_name = 'kivsee'
kivsee_logger = logging.getLogger(logger_name)

def init():
    if not kivsee_logger.hasHandlers():
        ch = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d | %(name)s | %(levelname)-07s | %(filename)-12s | %(funcName)s() line_%(lineno)s | %(message)s",
            datefmt='%d-%m-%Y %H:%M:%S')
        ch.setFormatter(formatter)
        kivsee_logger.addHandler(ch)
        kivsee_logger.setLevel(config.log_level)
        kivsee_logger.handler_set = True

init()
