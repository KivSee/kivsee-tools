import logging
import sys
from seqcreator import config

logger_name = 'kivsee'

kivseeLogger = logging.getLogger(logger_name)

def init():
    if not kivseeLogger.hasHandlers():
        ch = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d | %(name)s | %(levelname)s | %(filename)s:%(funcName)s() | line %(lineno)s | %(message)s",
            datefmt='%d-%m-%Y %H:%M:%S')
        ch.setFormatter(formatter)
        kivseeLogger.addHandler(ch)
        kivseeLogger.setLevel(config.log_level)
        kivseeLogger.handler_set = True


# def get_logger():
#     return logging.getLogger(logger_name)