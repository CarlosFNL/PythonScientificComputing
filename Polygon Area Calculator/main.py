class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter= 2*self.width + 2*self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width**2) + (self.height**2))**0.5
        return diagonal

    def get_picture(self):
        rect = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for i in range(0,self.height):
                rect += '*'*self.width + '\n'
            return rect
            
    def get_amount_inside(self,object):
        if self.get_area() >= object.get_area():
            area = self.get_area()
            area_to_fit = object.get_area()
            return (area//area_to_fit)
        else:
             return 0

class Square(Rectangle):
    def __init__(self,side):
        Rectangle.height = side
        Rectangle.width = side

    def __str__(self):
        return f'Square(side={Rectangle.height})'

    def set_side(self,side):
        Rectangle.height = side
        Rectangle.width = side

    def set_width(self,side):
        Rectangle.width = side
        Rectangle.height = side

    def set_height(self,side):
        Rectangle.height = side
        Rectangle.width = side



rect = Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))