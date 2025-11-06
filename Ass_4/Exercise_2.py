## Takes <parts> (tuple) and creates a dictionary in form of <part_number: (quantity, unit)>

inventory = {}
parts = [(1, '500-1', 'Hammer', 2, 'Pieces'), (2, '503', 'Screwdriver', 3, 'Pieces'), (3, '555', 'Nail', 10, 'Pieces')]

for item, part_number, name, quantity, unit in parts:
    inventory[part_number] = (quantity, unit)

print(inventory)