import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

async def main():
    await asyncio.gather(
        say_hello(),
        say_hello()
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
