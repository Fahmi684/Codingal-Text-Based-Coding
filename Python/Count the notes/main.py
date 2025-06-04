amount = int(input("Please input the number to withdraw: "))

note1 = amount//100
note2 = (amount%100)//50
note3 =((amount%100)%50)//10

print("Notes of 100tk: ", note1)
print("Notes of 50tk: ", note2)
print("Notes of 10tk: ", note3)