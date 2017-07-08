#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:56:50 2017
@author: Leonardo Fontes (@leonardofsales)

In a factory a printer prints labels for boxes. For one kind of boxes the
printer has to use colors which, for the sake of simplicity, are named with
letters from a to m.

The colors used by the printer are recorded in a control string.
For example a "good" control string would be aaabbbbhaijjjm meaning that
the printer used three times color a, four times color b, one time color h
then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and
a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm.

You have to write a function printer_error which given a string will
output the error rate of the printer as a string representing a rational
whose numerator is the number of errors and the denominator the length
of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only
letters from a to z.
"""


def printer_error(s):
    """
    Returns ratio of errors in a printer.
    """
    letters = [chr(l) for l in range(97, 110)]
    c = 0
    for l in s:
        if l not in letters:
            c += 1
    rate = str(c) + '/' + str(len(s))
    return rate

s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

print(printer_error(s))
