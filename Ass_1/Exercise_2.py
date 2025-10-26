## Converts dog years in human years
print('\nHello, dog-owner!')
print("Enter your dog's age and I will convert it into human age!")
dog_age = int(input('Enter dog age here => '))

if dog_age <= 0:
    print(f'\nYour dog can not be {dog_age} years old!\n')
elif dog_age == 1:
    human_age = 14
    print(f'\nYour dog is {human_age} years old in human years!\n')
elif dog_age == 2:
    human_age = 22
    print(f'\nYour dog is {human_age} years old in human years!\n')
else:
    human_age = 22 + 5 * (dog_age - 2)
    print(f'\nYour dog is {human_age} years old in human years!\n')