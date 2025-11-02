## Let user enter integers until they enter "stop"
## Returns Minimum, Maximum and Mean values

list_of_numbers = []

print(f'\nHello! Please enter a few numbers and I will provide you with:\nThe smallest input, the largest input and the mean value.\n')
while True:
    user_input = input('Please enter a number. If you wish to stop, enter <stop> => ')
    if user_input == 'stop':
        break
    list_of_numbers.append(int(user_input))

if list_of_numbers:
    print(f'\nThe smallest value is: {min(list_of_numbers)}')
    print(f'The largest value is: {max(list_of_numbers)}')
    print(f'The mean value is: {round(sum(list_of_numbers) / len(list_of_numbers), 2)}\n')
else:
    print('\nNo value was input!\n')