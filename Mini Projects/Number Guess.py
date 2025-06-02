print("Think of a number between 1 and 100. I will try to guess it!")
low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"My guess is {guess}.")
    feedback = input("Is it (h)igher, (l)ower, or (c)orrect? ").strip().lower()
    if feedback == 'c':
        print(f"Yay! I guessed your number in {attempts} tries.")
        break
    elif feedback == 'h':
        low = guess + 1
    elif feedback == 'l':
        high = guess - 1
    else:
        print("Please enter 'h', 'l', or 'c'.")