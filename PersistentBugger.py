#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 09:28:46 2017
@author: leonardofsales

Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in num until you reach a single digit.

"""

def persistence(n):
    c = 0
    while n >= 10:
        d = [int(d) for d in str(n)]
        r = 1
        for n in d:
            r = r * n
        n = r
        c += 1
    return c
            
print(persistence(9999))
