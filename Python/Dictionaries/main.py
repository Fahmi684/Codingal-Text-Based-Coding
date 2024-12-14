my_dict = {}
my_dict = {1: 'apple', 2:'Ball'}
my_dict = {'name': 'John', 1:[2, 3, 4]}
my_dict = {'name': 'John', 'age': 20}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 21
print(my_dict)

my_dict['address'] = 'DownTown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address: ", my_dict.get('address'))

my_dict.clear()
print(my_dict)