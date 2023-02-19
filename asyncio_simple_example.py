import asyncio
from typing import List
from http_request import async_request
from random import choice

countries = ["Canada", "Germany", "Italy", "Morocco", "Egypt", "Spain","Qatar", "China","Japan"]

async def get_universities(country_name: str) -> List:
    country_url = f"http://universities.hipolabs.com/search?country={country_name}"
    return await async_request(country_url)


async def main() -> None:
    country_name = choice(countries)
    universities = await get_universities(country_name)
    print(universities)


asyncio.run(main())
