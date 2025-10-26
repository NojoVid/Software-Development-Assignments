## Print a triangle based on the lenght provided by the user.

print('\nHello triangle enthusiast!')
print('Enter the lenght you want your triangle to be!')
tri_length = int(input('Enter triangle lenght here => '))

print('\n' + '=' * 20)

if tri_length <= 0 or tri_length > 7:
    print(f'\n{tri_length} is not a valid input!\n')
else:
    for n in range(1, tri_length + 1):
        print(n * '#')

    for i in range(1, tri_length):
        print((tri_length - i) * '#')

print('=' * 20 + '\n')