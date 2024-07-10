# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee(): #1
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5) #2
    print("coffee: ready")

async def fry_eggs(): #1
    print("egg: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) #2
    print("eggs: ready")

async def main(): #1
    start = time()
    coffee_task = asyncio.create_task(make_coffee()) #schedule execution
    eggs_task = asyncio.create_task(fry_eggs()) #schedule execution
    #wait for completion,both tasks are for execution already
    await make_coffee() #run task with await
    await fry_eggs()
    print(f"breakfast is ready in {time()-start} min")


asyncio.run(main()) #run top-level function concurrently