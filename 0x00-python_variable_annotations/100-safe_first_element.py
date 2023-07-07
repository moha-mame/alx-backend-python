#!/usr/bin/env python3
'''Task 10.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists.

    Args:
        lst: A sequence (list, tuple, etc.) containing elements of any type.

    Returns:
        The first element of the sequence if it is not empty, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
