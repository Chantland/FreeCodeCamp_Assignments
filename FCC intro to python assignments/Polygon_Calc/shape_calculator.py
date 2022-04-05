class Rectangle:
    def __init__(self, width, height):
        self.width = width                          # initial setting of width and height
        self.height = height
        self.isSquare = False
    def __str__(self):
        Rectangle_info = f'Rectangle(width={self.width}, height={self.height})'
        return Rectangle_info                       # display rectangle width and side
    def set_width(self, width):
        self.width = width
        if self.isSquare:                           #for child class square, the input of width affects height
            self.height = width
    def set_height(self, height):
        self.height = height
        if self.isSquare:                           #for child class square, the input of height affects width
            self.width = height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal
    def get_picture(self):
        Pict = ""
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        for Pict_Height in range(0, self.height):
            for Pict_Width in range(0, self.width):
                Pict += "*"
            Pict += "\n"
        return Pict
    def get_amount_inside(self, class_obj):
        fit_width = int(self.width / class_obj.width)   # get number of whole integer widths that could contain the sub-object width
        fit_height = int(self.height / class_obj.height) # do as above but for height
        fit_inside = fit_width * fit_height
        return fit_inside


class Square(Rectangle): # child object to Rectangle
    def __init__(self, dimensions):                 # redundancy to not make it call set_side only to call a different function
        self.isSquare = True
        self.set_width(dimensions)
    def __str__(self):
        square_info = f'Square(side={self.width})'  # since the width and height are the same, just give width
        return square_info                          # display square sides
    def set_side(self, dimensions):
        self.set_width(dimensions)
