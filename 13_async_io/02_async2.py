import asyncio 
import time

async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    print(f"{name} chai is ready")

async def main():
    await asyncio.gather(
        brew("masala"),
        brew("green"),
        brew("ginger"),
    )

start = time.time()
asyncio.run(main())
print(f"time taken is {time.time()-start:.2f} seconds")