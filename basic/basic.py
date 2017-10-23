""" Basic Logging Example """

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: '
                    '%(module)s: %(funcName)s: %(lineno)d: ',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def main():
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.critical('critical message')
    logging.error('error message')


if __name__ == '__main__':
    main()
