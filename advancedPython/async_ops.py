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


#2 use Threading
import threading
import requests
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s - %(asctime)s - %(levelname)s - %(message)s'
)

# Shared result list and lock
results = []
lock = threading.Lock()

def fetch_url(url):
    """The GIL is released during I/O operations!"""
    logging.info(f"Fetching URL: {url}")
    response = requests.get(url)
    content_length = len(response.content)
    logging.info(f"Completed: {url} (size: {content_length})")

    # Append result safely
    with lock:
        results.append(content_length)

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1", 
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1"
]

# Single-threaded
start = time.time()
results_single = [fetch_url(url) for url in urls]
single_time = time.time() - start

# Reset results
results = []

# Multi-threaded  
start = time.time()
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
multi_time = time.time() - start

logging.info(f"Single-threaded time: {single_time:.2f}s")  # ~4+ seconds
logging.info(f"Multi-threaded time: {multi_time:.2f}s")    # ~1 second
logging.info(f"Results collected: {results}")

# use multitasking
import multiprocessing
import requests
import time
import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(processName)s - %(asctime)s - %(levelname)s - %(message)s'
)

def fetch_url(url):
    logging.info(f"[PID {os.getpid()}] Fetching: {url}")
    response = requests.get(url)
    content_length = len(response.content)
    logging.info(f"[PID {os.getpid()}] Completed: {url} (size: {content_length})")
    return content_length

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1"
]

if __name__ == "__main__":
    # Single-process (sequential) benchmark
    start = time.time()
    results_single = [fetch_url(url) for url in urls]
    single_time = time.time() - start

    # Multi-process (parallel) benchmark
    start = time.time()
    with multiprocessing.Pool(processes=len(urls)) as pool:
        results_multi = pool.map(fetch_url, urls)
    multi_time = time.time() - start

    logging.info(f"Single-process time: {single_time:.2f}s")   # ~4+ seconds
    logging.info(f"Multi-process time: {multi_time:.2f}s")     # ~1 second
    logging.info(f"Results: {results_multi}")
