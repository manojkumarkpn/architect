##################### Chainmap ############################

"""
- Can flatten complexity, enhance readability
- ChainMap is a class in Python's collections module that groups multiple dictionaries (or mappings) together into a single, searchable view.
- ChainMap does this without copying data
- it's lightning-fast and memory-efficient.

# ChainMap vs Dictionary Merge (| Operator)
- Yes, Python 3.9+ supports the | operator to merge dicts:
- But that creates a new dictionary, unlike ChainMap, which is dynamic and linked.
- Any update in the original dicts reflects immediately in the ChainMap.
- Usefull when working with live or mutable state.

Sources:
1. https://medium.com/the-pythonworld/what-99-of-python-developers-dont-know-about-chainmap-and-why-it-s-a-game-changer-d40559dd9c37
2. 
"""
# ---------------------------------------------------
# Usecase 1: It searches keys in order, from first to last, returning the first match it finds.
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 30}
dict3 = {'b': 15, 'a': 5}
combined = ChainMap(dict1, dict2, dict3)
print(combined['b'])  # Output: 2 (from dict1, not dict2)
print(combined['c'])  # Output: 30 
print(combined['a'])  # Output: 30 

# ---------------------------------------------------
# Usecase 2:  Local Variable Scope Simulation
from collections import ChainMap
scopes = ChainMap()
scopes['x'] = 10

# Create a new inner scope
inner = scopes.new_child()
inner['x'] = 42

print(inner['x'])      # 42 (inner scope)
print(scopes['x'])     # 10 (outer scope)
# ---------------------------------------------------
# Usecase 3: Dynamic Context Injection
base_context = {'app_name': 'Python'}
user_context = {'user': 'Manoj'}

context = ChainMap(user_context, base_context)

def render(template, context):
    return template.format_map(context)

print(render("Welcome {user} to {app_name}!", context))
# Output: 'Welcome Manoj to Python!'
#################################################

