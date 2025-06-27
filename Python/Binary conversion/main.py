n = int(input("Enter a number:"))
mul = 1
result = 0
if n == 0:
    print(0)
else:
    while n > 1:
        rem = n%2
        result += rem*mul
        mul = mul*10
        n = int(n/2)
    print(result+1*mul)