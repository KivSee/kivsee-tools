import os
from dotenv import load_dotenv


load_dotenv()
name = os.getenv('NAME')
raspberry_pi_addr = os.getenv('RASPBERRY_ADDR')
object_service_port = os.getenv('OBJ_SERVICE_PORT')
sequence_service_port = os.getenv('SEQ_SERVICE_PORT')
trigger_service_port = os.getenv('TRIG_SERVICE_PORT')
log_level = os.environ.get('LOGLEVEL', 'INFO').upper()