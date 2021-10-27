#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    function named index_range that takes two integer arguments:
    page and page_size.
    The function should return a tuple of size two containing:
    a start index and an end index corresponding to
    the range of indexes to return in a list
    for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
