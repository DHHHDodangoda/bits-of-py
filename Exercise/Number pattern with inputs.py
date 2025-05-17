num = int( input('Enter a number: '))

for i in range (num,0,-1):
    print("*"*i)

# Enter a number: 5
# *****
# ****
# ***
# **
# *

#second method

for i in range (num,0,-1):
    for j in range (0,i):
        print("*",end="")
    print()

# *****
# ****
# ***
# **
# *
