class Student : 
    stream = 'csc'
    def __init__(self, roll):
        self.roll = roll

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address
    
add = Student(38)
add.setAddress("Dhaka, Bangladesh")
print(add.getAddress())

a = Student(38)
b = Student(76)

print(a.stream)
print(b.stream)
print(a.roll)
print( Student.stream )