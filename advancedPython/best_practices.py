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