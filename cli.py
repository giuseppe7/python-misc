#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import logging
import sys

'''
Main function of this script.
'''
def main():
    parser = argparse.ArgumentParser(add_help=False, description='Example command-line application.')
    parser.add_argument('-l', '--log-level', default='info', choices=['debug', 'info', 'warning', 'error', 'critical'])
    args = parser.parse_args()

    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
    log_datefmt = '%d/%b/%Y:%H:%M:%S %z'
    log_level = args.log_level.upper()
    log_level_num = getattr(logging, log_level.upper(), logging.INFO)
    logging.basicConfig(
        format=log_format,
        datefmt=log_datefmt,
        level=log_level_num
    )

    logging.debug('Starting main().')
    parser.print_help()
    logging.debug('Exiting main().')
    return 0

if __name__ == '__main__':
    sys.exit(main())
