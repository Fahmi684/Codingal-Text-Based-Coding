n = int(input("Enter a number:"))
digit = 0
temp = n

if n == 0:
    print("0 has 1 digit")
else:
    while temp > 0:
        temp //= 10
        digit += 1
    print(n, "has", digit, "digits")