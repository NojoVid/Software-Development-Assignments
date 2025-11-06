## Take <parts> (tuple) and gives part names

parts = [(1, '500-1', 'Hammer', 2, 'Pieces'), (2, '503', 'Screwdriver', 3, 'Pieces'), (3, '555', 'Nail', 10, 'Pieces')]

part_names = [name for item, part_number, name, quantity, unit in parts]
print(part_names)