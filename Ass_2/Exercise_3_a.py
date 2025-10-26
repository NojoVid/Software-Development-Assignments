## Prompt the user for a character and the number of times it should be repeated.
## Then generate a list showing the character repeated an ascending number of times.

print('\nHello! Please input a character and the number of times it should be repeted.')
user_char = str(input('Select a character. => '))

if len(user_char) == 0 or len(user_char) > 1:
    print(f'\nYou may only enter 1 character!\n')
else:
    user_numb = int(input('Select how many times to repeat it. => '))

    if user_numb <= 0:
        print(f'\n"{user_char}" can not be repeated {user_numb} times. :(\n')
    else:
        ascending_list = [user_char * i for i in range(1, user_numb + 1)]
            
        print('\n' + '=' * 20 + '\n')
        print(ascending_list)
        print('\n' + '=' * 20 + '\n')