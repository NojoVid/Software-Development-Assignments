## Take <given_list> and return ['H', 'E', 'L', 'L', 'O'] and ['P', 'E', 'T', 'E', 'R']

given_list = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']

hello_list = [item for index, item in enumerate(given_list) if index % 2 == 0]
print(hello_list)  # print(given_list[::2])

peter_list = [item for index, item in enumerate(given_list) if index % 2 != 0]
print(peter_list)  # print(given_list[1::2])