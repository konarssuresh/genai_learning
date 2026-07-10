import asyncio
import aiohttp


# https://lorem-api.com/api/article/foo

base_url = 'https://lorem-api.com/api/article/'


async def fetch_url(session, url):
    async with session.get(url,ssl=False) as response:
        print(f"fetched {url} with status {response.status}")

async def main():
    urls = [f"{base_url}f{i}" for i in range(10)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())