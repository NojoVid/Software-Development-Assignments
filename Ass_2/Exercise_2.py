## Prompt the user to enter k amount of words and calculates the lenght of of the combined words 

combined_lenght = 0

print('\nHello, broski!')
user_numb = int(input('How many words would you like to enter? => ')) # represents "k"

if user_numb <= 0:
    print(f'\n{user_numb} is not a valid input. Please try again.\n')
else:
    for number_of_words in range(1, user_numb + 1):
        user_word = input(f'\nEnter your {number_of_words}. word. => ')
        combined_lenght += len(user_word)
        
        print(f'\nThe combined lenght of the {user_numb} words entered is: {combined_lenght}\n')