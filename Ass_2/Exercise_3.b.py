## Multiply a number in sequence by factors stored in a list.

print("\nHello! Please enter a number and a list of factors, \nand I will multiply the number by each factor!")

user_number = float(input('\nEnter a number! => '))

user_input = input('\nEnter factors seperated by commas! => ')
user_factors = sorted([float(factor.strip()) for factor in user_input.split(',')])

factored_list = [round((user_number * factor), 2) for factor in user_factors]

print('\n' + '=' * 20 + '\n')
print(factored_list)
print('\n' + '=' * 20 + '\n')