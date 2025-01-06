def is_disarium(number):
    # Convert the number to a string to access its digits
    digits = str(number)
    # Calculate the sum of each digit raised to the power of its position
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    # Check if the sum equals the original number
    return disarium_sum == number

# Input number to check
num = int(input("Enter a number: "))
if is_disarium(num):
    print("%d is a Disarium number." % num)
else:
    print("%d is not a Disarium number." % num)
