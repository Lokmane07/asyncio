import asyncio
from typing import Dict
import requests


def sync_request(url: str) -> Dict:
    response = requests.get(url)
    return response.json()[0]


async def async_request(url: str) -> Dict:
    return await asyncio.to_thread(sync_request, url)