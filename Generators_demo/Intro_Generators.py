# Basic Introductions to working of generators

# Generators are functions that act like iterators

def func():
    return 1
    return 2
    return 3


print(func())

def gen():
    yield 1
    yield 2
    yield 3

print(gen())

# lets iterate over a generator func

for n in gen():         #On demand iteration
    print(n)