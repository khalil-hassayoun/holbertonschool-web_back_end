#!/usr/bin/env python3
""" a type-annotated function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a type-annotated function sum_list that
    takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    return sum(input_list)
