#intialize the variables
bill=0
units=0
taxbill=0

#Get the units from the user
units=int(input("Enter the number of units"))
bill=float(input("Enter the bill amount"))

#calculate the tax bill
taxbill= bill + (bill*(10/100))


#calculate and display the result
if units>60:
    print("THe bill amount is: ",taxbill)
else:
    print("The bill amount is: ",bill)


