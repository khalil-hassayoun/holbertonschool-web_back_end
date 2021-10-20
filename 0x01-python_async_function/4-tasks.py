#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called task_wait_n
    that takes in 2 int arguments:
    max_delay and n.
    You will spawn wait_random n times with the specified max_delay.
    """
    fcts = [
        task_wait_random(max_delay) for i in range(n)
    ]
    rs = []
    for x in asyncio.as_completed(fcts):
        r = await x
        rs.append(r)
    return rs
