class circle():
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
        return self.radius**2
    
new_radius = int(input("Enter radius:"))
new_circle = circle(new_radius)

print("Area of circle:", new_circle.circle_area(), "π")

class circle_perimeter():
    def __init__(self, r):
        r = new_radius
        self.radius = r

    def perimeter(self):
        return 2*new_radius
    
perimeter_circle = circle_perimeter()    
print("Area of circle:", new_circle.perimeter(), "π")