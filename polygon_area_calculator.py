class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, shape):
        # Calculate how many times the given shape can fit horizontally and vertically
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        return horizontal_fit * vertical_fit
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Call the parent class constructor with both width and height as side
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    # Override set_width to also set height for square
    def set_width(self, width):
        self.width = width
        self.height = width
    
    # Override set_height to also set width for square
    def set_height(self, height):
        self.width = height
        self.height = height
    
    def __str__(self):
        return f"Square(side={self.width})"


# Test the implementation with the provided usage example
if __name__ == "__main__":
    rect = Rectangle(10, 5)
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
