# Program that keeps logging something random
import random
import time
import logging
import logstash

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler('localhost', 50000, version=1))

while True:
    logger.info(f'[COLLISION_EVENT] Collision nr {random.randint(1, 25565)}')
    time.sleep(random.randint(10, 180))
    # End of program.
