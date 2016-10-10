#!/usr/bin/python
'''
This script welcomes the user if there is no name given. 
If no name, welcomes the whole world.
'''
import sys

def read_name():
    if len(sys.argv) >= 2:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'World'
    return name

def print_hello(given_name):
    print('Hello ' + given_name + '!')

name = read_name()
print_hello(name)