#Initialize the variables
hours=0
minutes=0
seconds=0
total_seconds=0

#Input the number of hours
hours = float(input("Enter the number of hours: "))
#Input the number of minutes
minutes = float(input("Enter the number of minutes: "))
#Input the number of seconds
seconds = float(input("Enter the number of seconds: "))

#Calculate the total number of seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

#Print the total number of seconds
print("The total number of seconds is", total_seconds)
