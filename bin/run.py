#!/usr/bin/env python

"""A simple python script template.

"""

import os
import sys
import argparse
import platform


def main(arguments):

    p = platform.system()
    if p == 'Linux':
        os.system('../manage.py runserver &')
        os.system('google-chrome --app="127.0.0.1:8000" --windows-size=800,600 & ')
    else:
        os.system('chrome.exe --app="127.0.0.1:8000" --windows-size=800,600')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
