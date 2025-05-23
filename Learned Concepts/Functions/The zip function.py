#The zip() function combines multiple iterables (like lists or tuples) into pairs, element by element.

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

'''Output:  Alice scored 85
            Bob scored 90
            Charlie scored 95
'''
