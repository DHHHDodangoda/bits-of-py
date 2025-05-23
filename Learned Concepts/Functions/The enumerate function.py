'''This adds a counter to an iterable and returns it as an enumerate object.
It’s useful when you need both the index and the value while looping.'''

names = ['Alice', 'Bob', 'Charlie']

for index, name in enumerate(names):
    print(f"{index}: {name}")

''' Output: 0: Alice
            1: Bob
            2: Charlie
'''

#If you need to start indexing with a custom number

for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")
  #This will start with 1 and go 2,3,4...
