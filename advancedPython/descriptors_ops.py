#
"""
A descriptor is a Python object that controls the behavior of attribute access — get, set, and delete — through a special protocol involving the methods
    __get__(self, instance, owner)

    __set__(self, instance, value)

    __delete__(self, instance)
Any object that implements at least one of these is a descriptor.

Descriptors enable:
    - Managed attributes (like validation or computation)
    - Shared behavior across many classes
    - The foundation of @property, staticmethod, classmethod, etc

Descriptors provide a way to:
    - Add logic to attribute access
    - Create computed or virtual attributes
    - Share reusable behavior via class-level objects
    - Implement proxies, lazy loading, type checking, caching, etc.

"""
# Implement both __get__ and __set__ Take precedence over instance dictionaries
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person:
    name = Typed('name', str)
    age = Typed('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 30)
print(p.name)  # Alice
p.age = 35     # OK
# p.age = "thirty-five"  # Raises TypeError

