#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine wait_random that
    takes in an integer argument
    (max_delay, with a default value of 10)
    and waits for a random delay between 0 and max_delay
    (included and float value) seconds
    and eventually returns it
    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
