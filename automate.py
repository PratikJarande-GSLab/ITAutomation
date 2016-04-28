#! /usr/bin/env python

"""
Entry point for App
Independent modules will be called from here
Modules will be:
1) ARG PARSER
"""
# project lib
from lib import argparser
from lib.ITLogger import Logger
logger = Logger().get_logger()

if __name__ == '__main__':
    kwargs = argparser.fetch()
    logger.info("ARG PARSING SUCCESSFUL\nKWARGS: {}".format(kwargs))


