lst = ["Apple", "Banana", "Kiwi", "Guava", "Mango"]

print("Lenght of list:", len(lst))
print("First element: ", lst[0])
print("Last element: ", lst[-1])

lst.append("Papaya")
print("Updated list: ", lst)

lst.remove("Kiwi")
print("Updated list: ", lst)

lst.sort()
print("Sorted list: ", lst)

lst.pop(1)
print("Updated list: ", lst)

lst.reverse()
print("Reversed list: ", lst)

print("Multiplication on list: ", lst*2)

lst = lst[:4]
print("Sliced list: ", lst)

lst.clear()
print("Updated list: ", lst)