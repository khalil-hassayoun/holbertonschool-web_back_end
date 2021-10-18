#!/usr/bin/env python3
""" a type-annotated function safely_get_value """
from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None])\
                     -> Union[Any, TypeVar('T')]:
    """ function safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
