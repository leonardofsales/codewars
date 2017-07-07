#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:51:09 2017
@author: Leonardo Fontes (@leonardofsales)
"""

# Problem:
# The new "Avengers" movie has just been released!
# There are a lot of people at the cinema box office standing in a huge line.
# Each of them has a single 100, 50 or 25 dollars bill.
# A "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk.
# He wants to sell a ticket to every single person in this line.
# Can Vasya sell a ticket to each person and give the change if he initially
# has no money and sells the tickets strictly in the order people follow
# in the line?
# Return YES, if Vasya can sell a ticket to each person and give the change.
# Otherwise return NO.


def tickets(people):
    """
    Returns YES or NO if clerk has change for $25 tickets.
    Considers the value of the bills (25, 50 or 100), not the total balance
    in the box.
    """
    b_25, b_50 = 0, 0
    for n in people:
        # No need of change for $25
        if n == 25:
            b_25 += 1
        # $50 requires $25 change
        elif n == 50:
            b_50 += 1
            if b_25 >= 1:
                b_25 = b_25 - 1
            else:
                return "NO"
        # $100 requires $50 + $25 or 3x$25
        elif n == 100:
            if (b_50 >= 1 & b_25 >= 1):
                b_50 = b_50 - 1
                b_25 = b_25 - 1
            elif (b_25 >= 3):
                b_25 = b_25 - 3
            else:
                return "NO"
    return "YES"
