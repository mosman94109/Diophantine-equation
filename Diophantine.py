#!/usr/bin/env python
"""
Avoid buying more than what you actually need.

Given a product which comes in 3 different package sizes, this script calcu-
lates the maximum amount (if any) which cannot be bought in exact quantity.

See https://en.wikipedia.org/wiki/Diophantine_equation.
"""

MAX = 200           # Some products do not have a maximum number. 
                    # We have to stop somewhere, although the 
                    # choice of initial quantity is arbitrary
                    
                    
bestSoFar = 0       # variable that keeps track of largest number
                    # of the product that cannot be bought in exact quantity
packages = (6, 9, 20)
assert packages[0] < packages[1] < packages[2]

def get_n(a, b, c):
    n = packages[0]*a + packages[1]*b + packages[2]*c
    return n

combo = {}

def check_if_combo_exists(num):    
    max_a = num/packages[0] + 2 # To avoid exceeding num
    max_b = num/packages[1] + 2 # " 
    max_c = num/packages[2] + 2 # "

    for a in range(0, max_a):
        for b in range(0, max_b):
            for c in range (0, max_c):
                if a + b + c ==0: continue
                if get_n(a, b, c) == i:
                    return 1
    return 0

ctr = 0
i = packages[0] + 1
while (ctr < packages[0] ) and (i <= MAX): # We stop checking when we encounter 
                                          # packages[0] (smallest package size) 
                                          # consecutive quantities that can 
                                          # be bought
    combo[i] = check_if_combo_exists(i)
    if combo[i]:
        ctr += 1
    else:
        ctr = 0
        bestSoFar = i
    i += 1

if (i == MAX) and (ctr <> packages[0] - 1): 
    print "Sorry, reached maximum number to try ({}).".format(MAX),
    print "Increase constant MAX if desired."
else:
    print "Max number: {}".format(bestSoFar)
