#!/usr/bin/env python3
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Create a directory and output the path for shell to cd into.',
        add_help=False
    )

    parser.add_argument(
        'dir_name',
        help='The directory name to create'
    )

    parser.add_argument(
        '-p', '--parent',
        action='store_true',
        help='Create parent directories as needed'
    )

    parser.add_argument(
        '-e', '--expand',
        action='store_true',
        help='Expand paths like ~, .., .'
    )

    parser.add_argument(
        '-s', '--silent',
        action='store_true',
        help='Output nothing, not even errors'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )

    parser.add_argument(
        '--configure-silence',
        choices=['err', 'cre'],
        help='Configure silence mode: err shows only errors, cre shows only file creation'
    )

    parser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit'
    )

    args = parser.parse_args()

    # Determine output mode
    silent = args.silent
    verbose = args.verbose
    config_silence = args.configure_silence

    if config_silence:
        if config_silence == 'err':
            silent = False
            verbose = False
        elif config_silence == 'cre':
            silent = False
            verbose = False

    # Process directory name
    dir_name = args.dir_name
    if args.expand:
        dir_name = os.path.expanduser(dir_name)
        dir_name = os.path.abspath(dir_name)

    # Output mode and directory name for shell to handle
    if silent:
        print("silent")
    elif verbose:
        print("verbose")
    elif config_silence == 'cre':
        print("cre")
    elif config_silence == 'err':
        print("err")
    else:
        print("default")
    
    print(args.parent)
    print(dir_name)

if __name__ == '__main__':
    main()
