# Madlibs game 

print("Welcome to the Madlibs game!")

# Get the user inputs
while True:
    adjective01 = input("Please enter an adjective: ")
    noun01 = input("Please enter a noun: ")
    adjective02 = input("Please enter another adjective: ")
    verb01 = input("Please enter a verb: ")
    adjective03 = input("Please enter one more adjective: ")

    # Create the story
    print ("Here is your story...\n")
    print (f"Today I went to a {adjective01} zoo. In the exhibit, I saw a {noun01}. {noun01} was {adjective02} and {verb01}. I was {adjective03}.")

    # Exit or play again
    while True:
        again = input("\nDo you want to play again (yes/no): \n").strip().lower()
        if again == 'yes':
            break
        elif again == 'no':
            print("\nThank You for playing...\n")
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
    if again == 'no':
        break
