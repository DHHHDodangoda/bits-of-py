
def caesar_encrypt(text, shift):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text.lower():
        if char in alphabet:
            index = (alphabet.index(char) + shift) % 26
            result += alphabet[index]
        else:
            result += char  # leave spaces and punctuation unchanged
    return result

text = str(input("Enter the text: "))
encrypted = caesar_encrypt(text, 3)
print("Encrypted text: ", encrypted)