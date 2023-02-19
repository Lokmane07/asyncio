import asyncio
from typing import List
from http_requests import get_async
from random import choice

countries = ["Canada", "Germany", "Italy", "Morocco", "Egypt", "Spain","Qatar", "China","Japan"]

async def get_universities(country_name: str) -> List:
    country_url = f"http://universities.hipolabs.com/search?country={country_name}"
    return await get_async(country_url)


async def main() -> None:
    country_name = choice(countries)
    universities = await get_universities(country_name)
    print(universities)


asyncio.run(main())
