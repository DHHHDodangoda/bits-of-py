#initialize the variables
number=0

#Get the number from the user
number=int(input("Enter your number: "))

#calculate and display the result
if number>10:
    print("The number one digit")
elif number>100:
    print("The numberhas two digits")
elif number>1000:
    print("The number has three digits")
else:
    print("The number has more than three digits")

