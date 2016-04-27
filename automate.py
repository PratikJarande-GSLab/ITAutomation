#! /usr/bin/env python
"""
Entry point for App
Independent modules will be called from here
"""

# projectlib
from lib import argparser


if __name__ == '__main__':
    kwargs = argparser.fetch()
    print("parsing success")
