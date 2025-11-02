numbers = [1, 4, 2, 8, 5]
squared_numbers = []

number = 0

while number < len(numbers):
    squared_numbers.append(numbers[number]**2)
    number += 1

print(squared_numbers)