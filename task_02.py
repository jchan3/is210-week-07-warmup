#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_02."""


def bool_to_str(bval):
    """A function that returns a 'yes' or 'no' value equivalent of truthy
        or falsy values.

    Args:
        bval(boolean): A boolean or boolean-like value that can be evaluated
        for truthiness or falsiness.

    Returns:
        str: A value of 'Yes' or 'No'.

    Examples:

        >>> task_02.bool_to_str(True)
        'Yes'

    """
    if bval is True:
        new_string = 'Yes'
    else:
        new_string = 'No'

    return new_string
