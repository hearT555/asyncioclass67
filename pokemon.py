import asyncio
import httpx
import time

async def get_ability(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    ability = resp.json()
    return ability

async def get_abilities():
    async with httpx.AsyncClient() as client:
        url = 'https://pokeapi.co/api/v2/ability/speed-boost'
        tasks = [asyncio.create_task(get_ability(client, url)) for _ in range(11)]
        
        abilities = await asyncio.gather(*tasks)
        return abilities

async def index():
    start_time = time.perf_counter()
    abilities = await get_abilities()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(abilities)} abilities. Time taken: {end_time-start_time} seconds")
    for i, ability in enumerate(abilities, 1):
        print(f"Ability {i}: {ability['name']}")
        print(f"Effect: {ability['effect_entries'][0]['effect']}")

if __name__ == '__main__':
    asyncio.run(index())
