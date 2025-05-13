'''The range() function is used to generate a sequence of numbers. It is commonly used in loops, especially for loops.

range(starting value, ending value, step value)'''

range(5)          # 0, 1, 2, 3, 4  
range(1, 6)       # 1, 2, 3, 4, 5
range(2, 10, 2)   # 2, 4, 6, 8
range(10, 0, -2)  # 10, 8, 6, 4, 2

#If it has only one value that must be the ending value 
#If it has two values first one has to be the starting value and the second one has to be ending value
#if it has three values first one has to be the starting value, the second one has to be ending value and the final one has to be the step value

for i in range(3):
    print(i)  # Output: 0, 1, 2
# end value will not be assigned to the variable so it is stop printing at (end value - 1)
