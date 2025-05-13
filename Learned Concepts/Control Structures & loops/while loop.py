
i = 0
while i in range(5):
    print(i)
    i += 1
# Output: 0, 1, 2, 3, 4

i = 2
while i in range(2, 10, 2):
    print(i)
    i += 2
# Output: 2, 4, 6, 8

#range() itself doesn’t control the loop — you must manually manage the counter (i).
#The loop runs as long as i is a valid value in the range object.

while True:
  print("Hello world")
  break

count = 0
while count <5:
  print(count)
  count=+1
print ("done")
# output: 0, 1, 2, 3, 4, done

