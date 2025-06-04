print("Enter marks obtained in 4 subjects:")
math = int(input("Math: "))
english = int(input("English: "))
science = int(input("Science: "))
history = int(input("History: "))

sum = math+english+science+history
perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)