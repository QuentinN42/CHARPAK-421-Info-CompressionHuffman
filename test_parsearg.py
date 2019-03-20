#!/usr/bin/python
# coding: utf-8

"""
Test du parseur d'arguments
"""

import argparse
import os

os.system('git rev-list --count HEAD > version')
with open('version', 'r') as f:
    __version__ = '1.' + f.read()



def parse_arguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Positional mandatory arguments
    parser.add_argument("Mode", help="Mode codage (C) ou decodage (D).", type=str)
    parser.add_argument("InputFile", help="Le fichier a coder ou decoder.", type=str)

    # Optional arguments
    parser.add_argument("-c", "--config", help="Fichier de configuration des frequences", type=str)
    parser.add_argument("-o", "--Output", help="Fichier de sortie (ecrase)", type=str)
    parser.add_argument("-ao", "--AppendOutput", help="Fichier de sortie (ecrit a la suite)", type=str)

    # Print version
    parser.add_argument("--version", action="version", version='Huffman - Version ' + __version__)

    # Parse arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    print(parse_arguments().InputFile)
