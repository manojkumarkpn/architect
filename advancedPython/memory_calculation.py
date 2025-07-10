#1 use memory_profiler
"""
Monitors line-by-line memory usage of functions using the @profile decorator.

Works well for tracking memory growth or leaks line-by-line.
"""
from memory_profiler import profile
@profile
def process_data():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del a
    return b

process_data()


#2 use tracemalloc
import tracemalloc

def allocate():
    a = [i for i in range(100000)]  # Some memory-heavy operation
    return a

tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()
allocate()
snapshot2 = tracemalloc.take_snapshot()

stats = snapshot2.compare_to(snapshot1, 'lineno')

for stat in stats[:3]:
    print(stat)



#3 pympler
"""
Pympler is a Python memory profiler that helps you:
    - Measure memory consumption of Python objects.
    - Identify memory leaks.
    - Track memory usage over time.
Understand object growth in long-running apps.
"""
from pympler import asizeof

class MyClass:
    def __init__(self):
        self.x = [i for i in range(1000)]

obj = MyClass()
print("Size in bytes:", asizeof.asizeof(obj))

from pympler import tracker
import time

mem_tracker = tracker.SummaryTracker()

# Run your program / simulation
for i in range(3):
    dummy = [j for j in range(i * 10000)]
    mem_tracker.print_diff()
    time.sleep(1)
