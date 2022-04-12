#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      5604254
#
# Created:     14/05/2018
# Copyright:   (c) 5604254 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import random

def randhexstr(len):   """a function that give a random hex for a given length"""
    hexl = []
    for i in range (10):
        hexl.append(i)
    let = ['a','b','c','d','e','f']
    for l in let:
        hexl.append(l)

    outL = []
    for i in range(len):
        outL.append(random.choice(hexl))

    outS = '#'
    for l in outL:
        outS = outS+str(l)
    return outS