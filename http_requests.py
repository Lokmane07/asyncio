import asyncio
from typing import Dict
import requests


def get_sync(url: str) -> Dict:
    response = requests.get(url)
    return response.json()[0]


async def get_async(url: str) -> Dict:
    return await asyncio.to_thread(get_async, url)