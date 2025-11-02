## Count how often the individual words of a text occur in it.

print('\nWrite a sentence and I will count how often a word appears in it.')
user_string = str(input('Enter a short sentence => '))
string_list = [word.strip('.,!?:') for word in user_string.split()]

counted_list = [f'{item}: {string_list.count(item)}' for item in string_list]

print('\n' + '<>' * 50)
if counted_list:
    print(', '.join(counted_list))
else:
    print('\nThere was no input!\n')
print('<>' * 50 + '\n')