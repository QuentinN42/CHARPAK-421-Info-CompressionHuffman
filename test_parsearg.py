#!/usr/bin/python
# coding: utf-8

import argparse


def parse_arguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Positional mandatory arguments
    parser.add_argument("creditMom", help="Credit mom.", type=float)
    parser.add_argument("creditDad", help="Credit dad.", type=float)
    parser.add_argument("debtMom", help="Debt mom.", type=float)

    # Optional arguments
    parser.add_argument("-dD", "--debtDad", help="Debt dad.", type=float, default=1000.)
    parser.add_argument("-s", "--salary", help="Debt dad.", type=float, default=2000.)
    parser.add_argument("-b", "--bonus", help="Debt dad.", type=float, default=0.)

    # Print version
    parser.add_argument("--version", action="version", version='%(prog)s - Version 1.0')

    # Parse arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    print(parse_arguments())
