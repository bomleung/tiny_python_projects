#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2023-08-08
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s','--sorted',action='store_true',default=False,help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items=args.item
    num=len(items)

    if args.sorted:
        items.sort()
    
    collection=''
    if num==1:
        collection=items[0]
    elif num==2:
        collection=' and '.join(items)
    else:
        items[-1]='and '+items[-1]
        collection=', '.join(items)

    print("You are bringing {}.".format(collection))


# --------------------------------------------------
if __name__ == '__main__':
    main()
