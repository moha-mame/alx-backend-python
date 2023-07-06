#!/usr/bin/env python3
'''Task 8
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Returns a function that multiplies a float by the given multiplier.
    '''

    def multiplier_function(num: float) -> float:
        '''
        Inner function that performs the multiplication.
        '''
        return num * multiplier

    return multiplier_function
