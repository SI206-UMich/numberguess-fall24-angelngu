import math

class Rectangle():
    # Create the constructor "__init__" method

    # YOUR CODE HERE
    def __init__(self,length, width):
        self.length = length
        self.width = width

    
    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"A rectange with width {self.length} and {self.width}"

    # Create the "area_calculator" method

    # YOUR CODE HERE
    def area_calculator(self):
        return self.width * self.length
        


    # Create the "__eq__" method
    # 
    # Returns a boolean value
    def __eq__(self,other):
        if self.width == other.width and self.height == other.height:
            return True
        else:
            return False 


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()