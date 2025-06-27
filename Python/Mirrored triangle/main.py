rows = int(input("Enter the number of rows:"))

print("Mirrored right angle triangle:")
for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()