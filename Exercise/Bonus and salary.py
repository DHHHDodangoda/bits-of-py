#initialize the variables
salery=0
years=0
bonus=0

#Get the salery and years from the user
salery = float(input("Enter your salery"))
years = int(input("Enter the number of years you have worked"))

#calculate and display the result
bonus = (salery * 12)+(5/100 * salery)

#print the result
if years>5:
    print("Your new salery with bonus is: ", bonus)
else:
    print("You have not worked long enough to get a bonus")

