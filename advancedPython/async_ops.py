#1 use asyncio
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

# This is the simplest and safest way to start an async program.
# Automatically creates and closes an event loop.
# Should only be used once in a program.
# Only works in the main thread.
asyncio.run(main())

# Gives you manual control over the event loop.
# Still used in older frameworks or specialized use cases.
# Avoid in new code — prefer asyncio.run() instead.
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
