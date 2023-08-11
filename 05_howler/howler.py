#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2023-08-11
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-case input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", type=str, help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", metavar="str", type=str, help="Output filename", default=""
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()