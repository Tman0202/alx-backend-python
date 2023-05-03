#!/usr/bin/env python3
'''Task 1 - Async Comprehensions'''


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that will collect 10 random numbers using an async
    comprehensing over async_generator, then returns the 10 random numbers.
    """
    collection = [i async for i in async_generator()]
    return collection
