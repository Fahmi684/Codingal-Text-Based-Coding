class CSStudent:
    stream = 'cse'
    def __init__(self, roll):
        self.roll = roll

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

add = CSStudent(101)
add.setAddress("Pune, Maharashtra")
print(add.getAddress())

a = CSStudent(101)
b = CSStudent(102)

print( a.stream ) # prints "cse"
print( b.stream ) # prints "cse"
print(a.roll) # prints 101

print( CSStudent.stream ) # prints "cse"