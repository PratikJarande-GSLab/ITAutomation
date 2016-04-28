""" Singleton Logger Implementation """
# -*- coding: utf-8 -*-

# stdlib
import logging
import os

LOG_FILE_DIR = os.path.join(os.path.abspath(os.sep), 'var', 'log', 'ITLog')
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, 'ITAutomation.log')


class Logger(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            return super(Logger, cls).__new__(cls, *args, **kwargs)
        else:
            return cls._logger

    def __init__(self):
        if hasattr(Logger, '_logger'):
            return

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Create logging format
        formatter = logging.Formatter(
            '-' * 80 + '\n' +
            '[PROCESS-ID: %(process)d PROCESS-NAME: %(processName)s ' +
            'THREAD-NAME: %(threadName)s]' + '\n' +
            '%(levelname)s in %(module)s [%(pathname)s]' + '\n' +
            '[%(asctime)s] FUNCTION %(funcName)s @ line %(lineno)d:' + '\n\n' +
            '%(message)s' + '\n' +
            '-' * 80 + '\n'
        )
        # Set formatter
        ch.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(ch)

        # Log File Checks
        if not os.path.exists(LOG_FILE_DIR):
            os.makedirs(LOG_FILE_DIR)
            # Create a file handler
            fh = logging.FileHandler(LOG_FILE_PATH)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        Logger._logger = self  # Assign this instance to `Logger._logger`

        msg = "Logger initialized successfully at {}".format(LOG_FILE_PATH)
        self.logger.info(msg)

    def get_logger(self):
        return self.logger
