# -*- coding: utf-8 -*-
# stdlib
import sys
import argparse
import json
from collections import OrderedDict

# project lib
from ITLogger import Logger
logger = Logger().get_logger()


# ============================
# Parse command line arguments
# ============================
def fetch():
    """
    Parse command line arguments and return user input
    :return: {<args>}
    """
    parser = argparse.ArgumentParser(
        description='Execute processes',
        epilog='Receives tasks from JSON file'
    )
    parser.add_argument(
        '-f',
        dest='file',
        required=True,
        help='JSON file that mentions the job in required format',
        action=LoadJSONFile,
    )
    return vars(parser.parse_args())


class LoadJSONFile(argparse._StoreAction):
    """
    To perform custom action on input params; need to subclass `Action`
    `_StoreAction` is the default Action

    Task of this Class:
    1) Validate JSON file path
    2) Convert file into JSON
    3) Convert JSON into OrderedDict
    4) Perform the default action
    """

    def __call__(self, parser, namespace, values, option_string=None):
        try:
            values = json.load(
                open(values, 'r'),
                object_pairs_hook=OrderedDict)
        except (IOError, OSError) as e:
            sys.stderr.write(
                "ERROR: Failed to load JSON File {} \n{}".format(values, e))
            sys.exit(1)

        # Perform default Action
        super(LoadJSONFile, self).__call__(
            parser, namespace, values, option_string)

