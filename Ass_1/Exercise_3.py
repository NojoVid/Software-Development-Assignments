## Calculates if a year is a leap year or not
print('\nHello dear leap year enthusiast!')
print('Enter a year and I will tell you if it is a leap year or not!')
year = int(input('Enter a year => '))

if year % 4 == 0 and year % 100 != 0:
    print(f'\n{year} is a leap year!\n')
elif year % 400 == 0:
    print(f'\n{year} is a leap year!\n')
else:
    print(f'\n{year} is not a leap year!\n')