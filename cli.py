#!/usr/bin/env python
import argparse

'''
Main function of this script.
'''
def main():
    parser = argparse.ArgumentParser(add_help=False, description='Example command-line application.')
    args = parser.parse_args()

    parser.print_help()

if __name__ == '__main__':
    main()
