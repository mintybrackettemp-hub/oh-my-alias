#!/usr/bin/env python3
import argparse
import os
import sys
import shutil

def main():
    parser = argparse.ArgumentParser(
        description='Remove current directory and cd to parent.',
        add_help=False
    )

    parser.add_argument(
        '-f', '--force',
        action='store_true',
        help='Forcefully remove the current folder (removes non-empty directories)'
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
        help='Configure silence mode: err shows only errors, cre shows only file removal'
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

    # Get current directory
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    dir_name = os.path.basename(current_dir)

    # Check if we're at root
    if current_dir == parent_dir:
        if not silent and config_silence != 'cre':
            print("Error: Cannot remove root directory", file=sys.stderr)
        sys.exit(1)

    # Output mode and directory info for shell to handle
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

    print(args.force)
    print(parent_dir)
    print(dir_name)

if __name__ == '__main__':
    main()
