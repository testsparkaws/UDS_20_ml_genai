import asyncio

async def fetch(site, secs):
    await asyncio.sleep(secs) # yields — other tasks can run!
    return f"got {site}"

async def main():
    t0 = asyncio.get_event_loop().time()
    results = await asyncio.gather(
        fetch("site-A", 1),    # all 3 start simultaneously
        fetch("site-B", 2),
        fetch("site-C", 1),
    )
    print(asyncio.get_event_loop().time() - t0)  # ≈ 2 seconds!

asyncio.run(main())