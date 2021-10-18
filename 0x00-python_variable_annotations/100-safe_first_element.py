#!/usr/bin/env python3
""" a type-annotated function safe_first_element """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function safe_first_element """
    if lst:
        return lst[0]
    else:
        return None
