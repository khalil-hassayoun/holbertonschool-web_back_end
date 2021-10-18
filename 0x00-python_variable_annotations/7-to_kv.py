#!/usr/bin/env python3
""" a type-annotated function to_kv """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a type-annotated function to_kv that
    takes a string k
    and an int OR float v as arguments
    and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and it's annotated as a float.
    """
    return (k, v ** 2)
