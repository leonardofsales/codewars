# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:52:35 2017

@author: Leonardo Fontes

@leonardofsales
"""


def square_digits(num):
    """
    Returns an integer consisting of the square of each digit of (num).
    The decimal marks are removed on floats, all digits are considered.
    """
    if type(num) is str:
        try:
            num = int(num)
        except:
            raise TypeError("Argument must be an int, a float or a string \
                            number.")
    elif type(num) is float:
        num = str(num).replace('.', '')

    return int(''.join(str(int(n)**2) for n in str(num)))
