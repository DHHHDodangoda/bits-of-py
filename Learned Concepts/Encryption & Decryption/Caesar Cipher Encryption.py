# fuction with two parameters 
def caesar_encrypt(text, shift):

    # Define the variables 
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text.lower():
        if char in alphabet:

            # Add shifting value to the text
            index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[index]
        else:
            
            # leave spaces and punctuation unchanged
            result += char  
    return result

# Get the inputs from the user
text = str(input("Enter the text: "))
shift = int(input("Enter your shifting value: "))

# Calling the function 
encrypted = caesar_encrypt(text, shift)
print("Encrypted text: ", encrypted)
