# Creating new lists

PrimaryList = [20,'Amal','Amara',39.534,80,"Mango"]
SecondaryList = ['item 01' , 'item 02' , 'item 03']

# Adding items to end of the list

PrimeryList.append("Orange")
print (PrimeryList)

# Adding items to a specific index

PrimeryList.insert(2,65) # in this method items dose not replace 
print (PrimeryList)

# replace items in a list

PrimeryList[0] = (42)
print (PrimeryList)

# Add new list to another list

PrimeryList.extend(SecondaryList)
print (PrimeryList)
