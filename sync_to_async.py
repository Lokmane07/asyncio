import asyncio
import time
import requests


async def counter(until: int = 10) -> None:
    end = time.perf_counter()
    print("Starting counter")
    for i in range(0, until):
        start = end
        await asyncio.sleep(0.01)
        end = time.perf_counter()
        print(f"{i}: Was asleep for {end - start}s")


def get_status_code(url: str) -> int:
    print("Sending request ")
    response = requests.get(url)
    return response.status_code


async def send_async_request(url: str) -> int:
    return await asyncio.to_thread(get_status_code, url)


async def main() -> None:

    status_code, _ = await asyncio.gather(
        send_async_request("http://universities.hipolabs.com/search?country=Canada"), counter()
    )
    print(f"Status code: {status_code}.")


asyncio.run(main())
