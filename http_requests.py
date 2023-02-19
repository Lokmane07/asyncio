import aiohttp
import asyncio
from typing import List
import requests


def get_sync(url: str) -> List:
    response = requests.get(url)
    return response.json()


async def get_async(url: str) -> List:
    return await asyncio.to_thread(get_sync, url)


async def get_async_aiohttp(url: str) -> List:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
