# Reading a File Line by Line (Lazily)
"""
Efficient: Doesn't load the entire file into memory.
Practical: Perfect for processing logs or large datasets.
Simple: Hides file-handling complexity inside the generator.
"""
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file("example.txt"):
    print(line)