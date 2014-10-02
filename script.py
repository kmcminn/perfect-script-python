#!/usr/bin/env python
#
# script.py - python script template
import sys
import argparse
import subprocess


def list_files(arg):
    """
    lists files using 'ls -l'
    """
    result = {}
    try:
        result['output'] = subprocess.check_output("ls -l " + arg, stderr=subprocess.STDOUT, shell=True)
        result['returncode'] = 0
    except subprocess.CalledProcessError, e:
        result['output'] = e.output
        result['returncode'] = e.returncode
    return result


def get_parser(name=sys.argv[0]):
    """
    returns an instance of OptionParser and added options
    """
    parser = argparse.ArgumentParser(description=name + " <options> ...")
    parser.add_argument('-l', '--list', dest='list', action='store',
                        help='an integer for the accumulator')
    return parser


def main():
    """
    parses argument from sys.argv and does work
    """
    if len(sys.argv) is 1:
        print get_parser().parse_args(['-h']).print_usage()
        return 1
    else:
        args = get_parser().parse_args(sys.argv[1:])
        if args.list:
            directory_listing = list_files(args.list)
            print directory_listing['output']
            return directory_listing['returncode']

    return 1

if __name__ == '__main__':
    sys.exit(main())