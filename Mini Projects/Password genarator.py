# A password generator

#importing necessary libraries
import random
import string

# Function to generate a random password
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define the character set based on user preferences
    characters = string.ascii_lowercase  # Always include lowercase letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password