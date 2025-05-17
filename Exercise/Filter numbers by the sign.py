#initializing the variables
list01=[10,23,24,35,65,78,90]
even=[]
odd=[]

for i in list01:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even numbers:',even)
print('Odd numbers:',odd)
# Even numbers: [10, 24, 78, 90]
# Odd numbers: [23, 35, 65]

