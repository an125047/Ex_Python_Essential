#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    print('Line 2')
    if True:
        print('Line 3')
    else:
        print('not in the if')

if __name__ == '__main__': main()
