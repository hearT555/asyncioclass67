import asyncio
import time

class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def PourCoffee():
    print(f"{time.ctime()} – Begin pour coffee...")
    time.sleep(2)
    print(f"{time.ctime()} – Finish pour coffee...")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} – Begin apply butter...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} – Finish apply butter...")

async def FryEggs(eggs):
    print(f"{time.ctime()} – Begin fry eggs...")
    print(f"{time.ctime()} – Heat pan to fry eggs")
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} – Frying", egg + 1, "eggs")
        await asyncio.sleep(1)
    print(f"{time.ctime()} – Finish fry eggs...")
    print(f"{time.ctime()} – >>>>>>>> Fry eggs are ready...")
    return Egg()

async def FryBacon():
    print(f"{time.ctime()} – Begin fry bacon...")
    await asyncio.sleep(2)
    print(f"{time.ctime()} – Finish fry bacon...")
    print(f"{time.ctime()} – >>>>>>>> Fry bacon is ready...")
    return Bacon()

async def ToastBread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(1)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>>> Toast are ready\n")
    return Toast()

def PourJuice():
    print(f"{time.ctime()} – Begin pour juice...")
    time.sleep(1)
    print(f"{time.ctime()} – Finish pour juice...")
    return Juice()

async def main():
    # Start pouring coffee first
    
    # Wait for coffee to finish before starting eggs
    PourCoffee()
    print(f"{time.ctime()} – >>>>>>>> Coffee is ready\n")
    
    # Start frying eggs and bacon concurrently
    eggs_task = asyncio.create_task(FryEggs(2))
    bacon_task = asyncio.create_task(FryBacon())
    
    # Start toasting bread concurrently
    toast_task = asyncio.create_task(ToastBread(2))
    
    
    await eggs_task
    print(f"{time.ctime()} – >>>>>>>> Fry eggs are ready\n")
    
    await bacon_task
    print(f"{time.ctime()} – >>>>>>>> Fry bacon is ready\n")
    
    await toast_task
    print(f"{time.ctime()} – >>>>>>>> Toast is ready\n")
    
    PourJuice()
    print(f"{time.ctime()} – >>>>>>>> Juice is ready\n")

if __name__ == "__main__":
    start_cooking = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} – Breakfast cooked in ", elapsed, "seconds.")
