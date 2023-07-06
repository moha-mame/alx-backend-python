#!/usr/bin/env python3
'''Task 7
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Converts a string and an int or float to a tuple.
    The first element of the tuple is the string `k`.
    The second element is the square of the int/float `v`.

    Args:
        k: A string.
        v: An int or float.

    Returns:
        A tuple with the string `k` and the square of `v` as a float.
    '''
    return (k, float(v ** 2))
