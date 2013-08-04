#!/usr/bin/env python
#
# perfect-script.py - a in-progress python script template
__version__ = '0.0.1'

import sys
import optparse

def parse_options(arguments=None):
    """
    parse arguments given to the script
    """
    if arguments is None:
        arguments = sys.argv

    parser = optparse.OptionParser(version=__version__,
                          usage="%prog [options] input ...")
    parser.add_option('-l', '--list', action="store_true",
                     help="list nodes by free disk space according to du data")

    return parser.parse_args(arguments[1:])


def main():
    """
    runs this script
    """
    options, args = parse_options()
    if options.list:
        print "list some files"

    return 0

if __name__ == '__main__':
    sys.exit(main())
