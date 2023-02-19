import asyncio
from random import choice
from time import perf_counter
from typing import Dict
from http_requests import get_async, get_sync, get_async_aiohttp

countries = ["Canada", "Germany", "Italy", "Morocco", "Egypt", "Spain", "Qatar", "China", "Japan"]


def get_random_country_universities_sync() -> Dict:
    country_name = choice(countries)
    country_url = f"http://universities.hipolabs.com/search?country={country_name}"
    universities = get_sync(country_url)
    return universities


async def get_random_country_universities_async() -> Dict:
    country_name = choice(countries)
    country_url = f"http://universities.hipolabs.com/search?country={country_name}"
    universities = await get_async(country_url)
    return universities


async def get_random_country_universities_async_aiohttp() -> Dict:
    country_name = choice(countries)
    country_url = f"http://universities.hipolabs.com/search?country={country_name}"
    universities = await get_async_aiohttp(country_url)
    return universities


async def main() -> None:

    # synchronous call
    time_before = perf_counter()
    for _ in range(20):
        get_random_country_universities_sync()
    print(f"Total time (synchronous): {perf_counter() - time_before}")

    # asynchronous call
    time_before = perf_counter()
    await asyncio.gather(*[get_random_country_universities_async() for _ in range(20)])
    print(f"Total time (asynchronous): {perf_counter() - time_before}")

    # asynchronous call (aiohttp)
    time_before = perf_counter()
    await asyncio.gather(*[get_random_country_universities_async_aiohttp() for _ in range(20)])
    print(f"Total time (asynchronous aiohttp): {perf_counter() - time_before}")

asyncio.run(main())
