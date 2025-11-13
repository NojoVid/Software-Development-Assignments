import random, time

user_number = int(input('\nSize of list/set => '))

list_random = random.sample(range(0, 10000001), user_number)
set_random = set(list_random)

benchmark_1 = time.time()

for _ in range(0, 1000):
    random_numb = random.randint(0, 10000001)
    random_numb in list_random

benchmark_2 = time.time()

for _ in range(0, 1000):
    random_numb = random.randint(0, 10000001)
    random_numb in set_random

benchmark_3 = time.time()

print(f'\nIt took {benchmark_2 - benchmark_1:.6f} to check the list.')
print(f'It took {benchmark_3 - benchmark_2:.6f} to check the set.\n')