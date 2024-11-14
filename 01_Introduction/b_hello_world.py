#!/usr/bin/python3
"""
Purpose: Basic PEP 8 guidelines and 
      shebang line

   PEP - Python Enhancement Prosopal
   PEP 8 - coding style guide

This is docstring

"""
# print as a statement in python 2
# print "Hello world!"

# print as a function in python 2 & 3
print("Hello world!")
print(True)
print("True", 123, None)

def wishes (name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("Udhay")