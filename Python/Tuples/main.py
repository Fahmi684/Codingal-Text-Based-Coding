my_tuple = {}
print(my_tuple)

my_tuple = {1, 2, 3}
print(my_tuple)

my_tuple = {1, 'Hello', 2, 3}
print(my_tuple)

my_tuple = ("mouse", [4, 5, 6], (1, 2, 3))
print(my_tuple)

my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index

print(n_tuple[0][3])

print(n_tuple[1][1])

# Slicing

print("Sliced ​​:", my_tuple[1:4])

# Iterating through tuple

for letter in (my_tuple):

    print("Hello", letter)