## Takes two lists of first and last names and combines then into a list called <names>

first_names = ['Jane', 'Max', 'Giannis', 'Juan']
last_names = ['Doe', 'Mustermann', 'Karamitros', 'Perez']

names = list(zip(first_names, last_names))

print(names)

# This is not the optimal approach
# Both lists need to have matching lenght and order
# Tuples can access both first and last name from a single list