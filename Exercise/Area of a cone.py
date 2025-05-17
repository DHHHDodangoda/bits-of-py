#Import the math module
import math

#Initialize the variables
radius=0
height=0
volume=0

#Input the radius of the cone
radius = float(input("Enter the radius of the cone: "))
#Input the height of the cone
height = float(input("Enter the height of the cone: "))

#Calculate the volume of the cone
volume = 1/3 * math.pi * radius * radius * height

#Print the volume of the cone
print("The volume of the cone is", volume)
