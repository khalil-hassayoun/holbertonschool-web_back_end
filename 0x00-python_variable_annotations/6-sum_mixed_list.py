#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a type-annotated function sum_mixed_list that
    takes a list mxd_lst of floats and integers as argument
    and returns their sum as a float.
    """
    return sum(mxd_lst)
