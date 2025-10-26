## Take a list of integers and seperates it into even and odd numbers.

print('\nHello! Provide me with a list of numbers and I will sort them into EVEN and ODD numbers!')
user_input = input('Enter numbers seperated by commas! => ')

user_numbers = [int(number.strip()) for number in user_input.split(',')]

even_list = sorted([number for number in user_numbers if (number % 2 == 0)])
odd_list = sorted([number for number in user_numbers if (number % 2 != 0)])

print('\n' + '=' * 20 + '\n')
print(f'All even numbers are: {even_list}')
print(f'All odd numbers are: {odd_list}')
print('\n' + '=' * 20 + '\n')