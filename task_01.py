#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01"""


def fibonacci(maxint):
    """Use a while loop to make a Fibonacci sequence.

    Args:
        maxint(int): An integer that serves as the upper bound of the loop.

    Returns:
        new_list: A list of a Fibonacci sequence up to maxint.

    Examples:

        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

    """
    new_list = [0]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        new_list.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return new_list
