import os
from dotenv import load_dotenv


load_dotenv()
user_name = os.getenv('USER_NAME')
raspberry_pi_addr = os.getenv('RASPBERRY_ADDR')
object_service_port = os.getenv('OBJ_SERVICE_PORT')
sequence_service_port = os.getenv('SEQ_SERVICE_PORT')
trigger_service_port = os.getenv('TRIG_SERVICE_PORT')
log_level = os.environ.get('LOGLEVEL', 'INFO').upper()
brightness_level = os.getenv('BRIGHTNESS_LEVEL')

if brightness_level == None:
    brightness_level = 1.0
