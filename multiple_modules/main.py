"""Logging example for multiple modules"""

import logging
import os
import threading
import time

from worker import worker

try:
    os.environ['MY_LOGGING_LEVEL']
except:
    level = logging.INFO
else:
    level = logging.DEBUG

logging.basicConfig(level=level,
                    format='[%(levelname)s]'
                    '%(threadName)-15s %(message)s')


def main():
    w1_thread = threading.Thread(target=worker, name='worker')
    w2_thread = threading.Thread(target=worker)
    w3_thread = threading.Thread(target=worker)

    w2_thread.start()
    w1_thread.start()
    w3_thread.start()

    main_thread = threading.main_thread()

    for t in threading.enumerate():
        if t == main_thread:
            continue
        t.join()


if __name__ == '__main__':
    logging.info('starting')
    start = time.time()
    main()
    end = time.time()
    logging.debug(end - start)
    logging.info('Exiting')
