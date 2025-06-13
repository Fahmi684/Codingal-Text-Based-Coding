medical_cause = str(input("Did you have a medical cause Y or N:"))

if medical_cause == "Y":
    print("You are allowed")
elif medical_cause == "N":
    attend = int(input("Enter the attendance of the student:"))
    if attend == 75:
        print("You are allowed")
    else:
        print("You are not allowed")
else:
    print("Wrong input")