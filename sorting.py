#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input
which controls how the elements of the list should be compared against each other:
If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''

import random
from copy import copy

def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    mergedlist = []
    x_index = 0
    y_index = 0
    while x_index < len(xs) and y_index < len(ys):
        check = cmp(xs[x_index],ys[y_index])
        if check == -1:
            mergedlist.append(xs[x_index])
            x_index += 1
        if check == 1:
            mergedlist.append(ys[y_index])
            y_index += 1
        if check == 0:
            mergedlist.append(xs[x_index])
            x_index += 1
            mergedlist.append(ys[y_index])
            y_index += 1

    if x_index < len(xs):
        mergedlist += xs[x_index:]
    if y_index < len(ys):
        mergedlist += ys[y_index:]
    return mergedlist


def merge_sorted(xs, cmp=cmp_standard):
    real_xs = copy(xs)
    if len(real_xs) <= 1:
        return real_xs
    else:
        half = len(real_xs) // 2
        left = merge_sorted(real_xs[:half], cmp)
        right = merge_sorted(real_xs[half:], cmp)
        return _merged(left, right)

def quick_sorted(xs, cmp=cmp_standard):
    '''
    '''
    real_xs = copy(xs)
    if len(real_xs) <= 1:
        return real_xs
    else:
        p = random.choice(real_xs)
        less = []
        greater = []
        equal = []
        for num in real_xs:
            if num < p:
                less.append(num)
            elif num > p:
                greater.append(num)
            else:
                equal.append(num)
        return quick_sorted(less, cmp) + equal + quick_sorted(greater, cmp)
        

def quick_sort(xs, cmp=cmp_standard):
    '''
    '''
