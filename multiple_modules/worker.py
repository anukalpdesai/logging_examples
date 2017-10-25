import logging
import time


def worker():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')
