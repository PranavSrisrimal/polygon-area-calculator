class Rectangle: 
    
    def __init__(self, width, height):
        self.width = width
        self.height = height        

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width 

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else :
            shape=""
            for i in range(self.height):
                    shape += "*" * self.width
                    shape += "\n"
            return shape

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
                          

    def get_amount_inside(self,shape):
        area = self.get_area()
        shape_area = shape.get_area()

        return int(area/shape_area)

class Square(Rectangle):
    
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
      
    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)    

    def __str__(self):
         return "Square(side={})".format(self.side)