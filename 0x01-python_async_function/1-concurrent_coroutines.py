#!/usr/bin/env python3
'''Task 1
'''
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Asynchronous coroutine function that waits for n random delays.
    '''
    delay = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay)
