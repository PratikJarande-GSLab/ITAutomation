# stdlib
import argparse
import json
import pprint


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
        '-f', dest='file', required=True, #type=json.loads,
        help='JSON file that mentions the job in required format',
        metavar='job.json', action=LoadJSONFile,
        type=json.load(argparse.FileType('r'))
    )
    return vars(parser.parse_args())


class LoadJSONFile(argparse.Action):
    def __call__(self, *args, **kwargs):

        print("ARGS: \n{}".format(args))
        print("\nKWARGS: \n{}".format(kwargs))


        # print("{}.{}".format(pprint.pformat(args), pprint.pformat(kwargs)))
