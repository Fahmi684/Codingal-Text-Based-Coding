cp = int(input("Enter the cp:"))
sp = int(input("Enter the sp:"))

if(sp>cp):
    print("profit")
    pt = sp-cp
    print(pt)
else:
    print("No profit")