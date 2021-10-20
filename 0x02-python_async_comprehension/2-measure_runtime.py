#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime is a coroutine
    that will execute async_comprehension four times in parallel
    using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    """
    t0 = time.time()
    fcts = [async_comprehension() for i in range(4)]
    await asyncio.gather(*fcts)

    return time.time() - t0
