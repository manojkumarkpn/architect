""" 
References
- https://medium.com/@abdur.rahman12/10-outdated-python-practices-you-need-to-stop-using-right-now-8dd688e01045
- 
"""
#1 Using == None Instead of is None
x = None
if x is None:
    print(x)

#2 Writing Loops Where List Comprehensions Would Shine
squares = []
for i in range(10):
    squares.append(i ** 2)

squares = [i ** 2 for i in range(10)]

#3 Hardcoding File Paths
from pathlib import Path
path = Path.home() / "Documents" / "script.py"

#4  Overusing print() for Debugging
breakpoint()

#5 Catching specific Exception  
try:
    do_something()
except FileNotFoundError:
    print("File not found. Check the path.")

#6 use enumerate
for i, val in enumerate(my_list):
    print(i, val)

#7 Mutable Default Arguments in Functions
def append_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

#8 Manually Managing Resources Instead of Using Context Managers
with open('data.txt') as f:
    data = f.read()

#9 Import specific methods and classes
from math import sqrt, pi

#10 use data types
def calculate_area(radius: float) -> float:
    return math.pi * radius ** 2

#11 Use Generators and yield
"""
- A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
- Instead of returning all values at once (like a list does), a generator produces values one at a time, on the fly, using the yield keyword.
- This is crucial for large data processing or streaming applications.
"""
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1
for number in count_up_to(5):
    print(number)

#12 use decorators
""" 
- Decorators are functions that modify the behavior of other functions — think logging, timing, caching, or access control.
- Decorators help you implement cross-cutting concerns cleanly and elegantly.
"""
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}")


#13 use conext manager to safely initialize and destroy  instance
"""
Resource safety: Avoids leaving PJSIP running if an exception occurs.

Cleaner code: No need to manually destroy PJSIP outside the block.

Reusable: You can use this pattern in any script that needs temporary PJSIP access.
"""
import pjsua as pj
from contextlib import contextmanager

@contextmanager
def pjsip_library():
    lib = pj.Lib()

    try:
        lib.init()
        lib.create_transport(pj.TransportType.UDP)
        lib.start()
        print("PJSIP started.")
        yield lib
    finally:
        lib.destroy()
        lib = None
        print("PJSIP shut down.")

with pjsip_library() as lib:
    # You can register an account, make calls, etc.
    # This is just an example placeholder:
    print("Do SIP operations here...")