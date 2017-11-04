#!/usr/bin/env python3

from login import sign_in
import argparse


def __main(args):
    response = sign_in(args.login, args.password)


def __parse_args():
    parser = argparse.ArgumentParser(description='Clock in and out of pontomais.')
    parser.add_argument('-l', '--login', metavar='login', type=str, nargs=1,
                        help='login for the user')
    parser.add_argument('-p', '--password', metavar='password', type=str, nargs=1,
                        help='password for the user')

    return parser.parse_args()


if __name__ == '__main__':
    __main(__parse_args())
