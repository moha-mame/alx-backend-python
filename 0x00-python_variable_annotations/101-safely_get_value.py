#!/usr/bin/env python3
'''Task 11
'''
from typing import Any, Mapping, Union


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """
    Safely retrieves a value from a dictionary based on the provided key.

    Args:
        dct: A dictionary with keys of type K and values of type V.
        key: The key to look up in the dictionary.
        default: The default value to return if the key is not found.

    Returns:
        The value from the dictionary if the key exists, or the default value (or None).
    """
    if key in dct:
        return dct[key]
    else:
        return default
