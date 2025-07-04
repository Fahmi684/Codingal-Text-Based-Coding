def add(p, q):
    return p+q
def subtract(p, q):
    return p-q
def multiply(p, q):
    return p*q
def divide(p, q):
    return p/q

print("Please select an operation:")
print("a. Add")
print("b. subtract")
print("c. multiply")
print("d. divide")
choice = input("Select an action:")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if choice=="a":
    print(num1, "+", num2, "=", add(num1, num2))
if choice=="b":
    print(num1, "-", num2, "=", subtract(num1, num2))
if choice=="c":
    print(num1, "*", num2, "=", multiply(num1, num2))
if choice=="d":
    print(num1, "/", num2, "=", divide(num1, num2))