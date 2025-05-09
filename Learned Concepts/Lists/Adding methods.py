# Creating new lists

PrimaryList = [20,'Amal','Amara',39.534,80,"Mango"]
SecondaryList = ['item 01' , 'item 02' , 'item 03']

# Adding items to end of the list

PrimaryList.append("Orange")
print (PrimaryList)

# Adding items to a specific index

PrimaryList.insert(2,65) # in this method items dose not replace 
print (PrimaryList)

# replace items in a list

PrimaryList[0] = (42)
print (PrimaryList)

# Add new list to another list

PrimaryList.extend(SecondaryList)
print (PrimaryList)
