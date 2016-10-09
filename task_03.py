#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_03."""


import decimal


def lexicographics(to_analyze):
    """A function that provides the maximum, minimum, and average number
        of words in a speech.

    Args:
        to_analyze(str): A string of sentences in a speech.

    Returns:
        tuple: A tuple with the maximum, minimum, and average number of words
        per line.

    Examples:

        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4'))

    """
    count_list = []
    for line in to_analyze.split('\n'):
        word_count = len(line.split(' '))
        count_list.append(word_count)

    max_words = max(count_list)
    min_words = min(count_list)
    avg_words = (decimal.Decimal(sum(count_list)))/len(count_list)
    return (max_words, min_words, avg_words)
