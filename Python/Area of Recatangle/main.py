class rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def rectangle_area(self):
        return self.length*self.width
    
NewRectangle = rectangle(10, 11)
print("Dimension of rectangle- Length: %d Width: %d" % (NewRectangle.length, NewRectangle.width))
print("Area of rectangle:", NewRectangle.rectangle_area())