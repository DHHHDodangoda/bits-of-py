count=0
list01=[111,32,-9,-45,-17,9,85,-10 ]
list02=[]

while ( count <len(list01)):
    if (list01[count] > 0):
        list02.append(list01[count])
    count+=1
print(list02)
