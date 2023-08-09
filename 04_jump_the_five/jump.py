#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2023-08-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    jumpString=args.text

    table=dict()

    table['1']='9'
    table['2']='8'
    table['3']='7'
    table['4']='6'
    table['5']='0'
    table['6']='4'
    table['7']='3'
    table['8']='2'
    table['9']='1'
    table['0']='5'


    outText=''

    for char in jumpString:
        outText+=table.get(char,char)

    print('{}'.format(outText))
   


# --------------------------------------------------
if __name__ == '__main__':
    main()
