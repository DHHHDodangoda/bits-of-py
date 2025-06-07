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
# Main function to run the password generator
def main():
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n, default is y): ").strip().lower() != 'n'
    use_numbers = input("Include numbers? (y/n, default is y): ").strip().lower() != 'n'
    use_special_chars = input("Include special characters? (y/n, default is y): ").strip().lower() != 'n'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()