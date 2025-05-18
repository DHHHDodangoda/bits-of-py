#List comprehension is a concise way to create lists using a single line of code.

squares = [x**2 for x in range(5)]
print(squares)

#Output [0, 1, 4, 9, 16]

''' With a condition '''

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#Output [0, 2, 4, 6, 8]
