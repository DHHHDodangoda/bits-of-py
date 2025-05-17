#initialize the variables
held=0
attended=0

#get the inputs from the user
held=int(input("Number of classes held"))
attended=int(input("Number of classes attended"))

#calculate and display the results
if (held/attended)*100>70:
    print("You can sit for the exam")
else:
    print("You cannot sit for the exam")

