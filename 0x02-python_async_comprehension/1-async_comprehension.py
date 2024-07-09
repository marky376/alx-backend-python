#!/usr/bin/env python3

from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]

