string = input("Enter a string:")
string2 = ("")

for i in string:
    string2 = i + string2

print("\n the original string:", string)
print("The reversed string:", string2)