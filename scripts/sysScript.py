#!/usr/bin/env python
# Example of sys.argv to access command line args
import sys

def main():
    for arg in sys.argv:
        print(arg)
    
    # Set exit return code.
    sys.exit(0)

main()