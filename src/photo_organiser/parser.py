import argparse
from pathlib import Path


# TODO: expand help messages for arguments
def parse_args(args):
    # create argument parser to read source and destination directories
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path, help='Source directory of unsorted images')
    parser.add_argument('dest', type=Path, help='Destination directory of sorted images')
    return parser.parse_args(args)
