## Guessing game optimized (hopefully)

import random

attempts_used = 0
amount_tries = 0
interval_list = []

print('\nHello. Please enter an interval in the style of lower, upper')

while True:  # User input
    user_interval = input('Enter interval here! => ')

    if not user_interval:
        print('\nYou must enter an interval to continue. (Remember: lower, upper)')
        continue
        
    interval_list = [int(number.strip()) for number in user_interval.split(',')]

    if len(interval_list) != 2:
        print('\nYour interval needs to contain 2 numbers. (Remember: lower, upper_part)')
        continue
    elif interval_list[0] >= interval_list[1] or interval_list[0] < 0:
        print(f'\n"{user_interval}" is not a valid input. Please try again. (Remember: lower, upper)')
        continue

    break

secret_number = random.randint(interval_list[0], interval_list[1])

print('\nWould you like to have a limited amout of tries? (Y/N)')
while amount_tries == 0:  # Asks user to choose between Limited and Unlimited guessing game
    user_choice = input('Choose => ').strip().upper()

    if user_choice == 'Y' or user_choice == 'YES':
        print('\nHow many times would you like to try?')
        user_choice = int(input('Choose => '))
        amount_tries += user_choice

        while amount_tries > attempts_used:  # Limited guessing game
            print(f'\nAmount of tries left: {amount_tries - attempts_used}')
            guess_number = input(f'Guess a number between {interval_list[0]} and {interval_list[1]}. => ')
            
            if not guess_number:
                print('\nYour NEED to guess!')
                continue
            elif interval_list[0] > int(guess_number) or interval_list[1] < int(guess_number):
                print(f'\nYour guess needs to be between the interval of {interval_list[0]} and {interval_list[1]}!')
                continue

            attempts_used += 1

            if int(guess_number) == secret_number:
                print(f'\nYou got it! {secret_number} was the secret number!')
                print(f'Amount of tries: {attempts_used}\n')
                break

            if amount_tries == attempts_used:
                print(f'\nYou have no more tries... The secret number was {secret_number}.\n')
                break  

            if int(guess_number) < secret_number:
                print('\nToo low! Guess again.')
            elif int(guess_number) > secret_number:
                print('\nToo high! Guess again.')

    elif user_choice == 'N' or user_choice == 'NO':        
        while True:  # Unlimited guessing game
            guess_number = input(f'\nGuess a number between {interval_list[0]} and {interval_list[1]}. => ')

            if not guess_number:
                print('\nYour must guess!')
                continue
            elif interval_list[0] > int(guess_number) or interval_list[1] < int(guess_number):
                print(f'\nYour guess needs to be between the interval of {interval_list[0]} and {interval_list[1]}!')
                continue
            
            amount_tries += 1

            if int(guess_number) < secret_number:
                print('\nToo low! Guess again.')
            elif int(guess_number) > secret_number:
                print('\nToo high! Guess again.')
            else:
                print(f'\nYou got it! {secret_number} was the secret number!')
                print(f'Amount of tries: {amount_tries}\n')
                break

    else:
        print('\nYou need to enter Y (for yes) or N (for no).')
        continue