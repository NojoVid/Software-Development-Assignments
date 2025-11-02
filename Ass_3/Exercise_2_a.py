customers = [
["Max", "Mustermann", "01.01.83"],
["Martina", "Musterfrau", "02.02.84"],
["Gabi", "Meier", "03.03.85"]
]

last_names = []

for person in customers:
    last_names.append(person[1])

print(last_names)