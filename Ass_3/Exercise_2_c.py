import random
secret_number = random.randint(1, 100) # Generate random number

for x in range(1,101):
    guess = int(input(f"Your {x}. try. Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high! Guess again.")
    elif guess < secret_number:
        print("Too low! Guess again.")
    else:
        print("You guessed it! The number was", secret_number)
        break